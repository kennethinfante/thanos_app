from PyQt5.QtWidgets import QMainWindow, QMessageBox, QPushButton
from PyQt5.QtCore import QDate
from datetime import datetime
from forms_python.invoice_view_edit import Ui_viewEditInvoice
from src.dao.invoice_dao import InvoiceDao
from src.dao.customer_dao import CustomerDao
from src.models.invoice_lines_model import InvoiceLinesModel
from src.do.invoice import InvoiceLine

class ViewInvoice(QMainWindow):
    def __init__(self, invoice_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_viewEditInvoice()
        self.ui.setupUi(self)

        self.invoice_id = invoice_id
        self.invoice_dao = InvoiceDao()
        self.customer_dao = CustomerDao()

        # Create the invoice lines model
        self.invoice_lines_model = InvoiceLinesModel(invoice_id)

        # Load invoice data
        self.invoice = self.invoice_dao.get_invoice_with_lines(invoice_id)

        # Initialize UI components
        self.initialize_ui()
        self.connect_signals_slots()

    def initialize_ui(self):
        """Initialize UI with invoice data"""
        if not self.invoice:
            QMessageBox.critical(self, "Error", "Invoice not found")
            self.close()
            return

        # Set window title
        self.setWindowTitle(f"Invoice #{self.invoice.invoice_number}")

        # Set invoice number label
        self.ui.invoice_number_label.setText(f"Invoice #{self.invoice.invoice_number}")

        # Load customers into combobox
        self.load_customers()

        # Set customer
        if self.invoice.customer:
            index = self.ui.customer_cb.findData(self.invoice.customer.id)
            if index >= 0:
                self.ui.customer_cb.setCurrentIndex(index)

        # Set dates
        if self.invoice.date:
            self.ui.invoice_date_edit.setDate(QDate.fromString(self.invoice.date.strftime("%Y-%m-%d"), "yyyy-MM-dd"))

        if self.invoice.due_date:
            self.ui.due_date_edit.setDate(QDate.fromString(self.invoice.due_date.strftime("%Y-%m-%d"), "yyyy-MM-dd"))

        # Load invoice lines
        self.load_invoice_lines()

        # Add buttons for adding and removing invoice lines
        self.add_invoice_line_buttons()

    def load_customers(self):
        """Load customers into the customer combobox"""
        self.ui.customer_cb.clear()
        customers = self.customer_dao.get_all_customers()

        for customer in customers:
            self.ui.customer_cb.addItem(customer.name, customer.id)

    def load_invoice_lines(self):
        """Load invoice line items into the table view"""
        # Set the model for the invoice lines table view
        self.ui.invoice_lines_table_view.setModel(self.invoice_lines_model)

        # Adjust column widths for better display
        # ["Item", "Account", "Description", "Quantity", "Unit Price", "Subtotal", "Tax Amount", "Line Amount"]
        self.ui.invoice_lines_table_view.setColumnWidth(0, 150)
        self.ui.invoice_lines_table_view.setColumnWidth(1, 150)
        self.ui.invoice_lines_table_view.setColumnWidth(2, 200)
        self.ui.invoice_lines_table_view.setColumnWidth(3, 100)
        self.ui.invoice_lines_table_view.setColumnWidth(4, 100)
        self.ui.invoice_lines_table_view.setColumnWidth(5, 100)
        self.ui.invoice_lines_table_view.setColumnWidth(6, 100)
        self.ui.invoice_lines_table_view.setColumnWidth(7, 100)

    def add_invoice_line_buttons(self):
        """Add buttons for adding and removing invoice lines"""
        # Create a button for adding a new line
        self.add_line_btn = QPushButton("Add Line", self)
        self.add_line_btn.setMinimumSize(115, 30)
        self.add_line_btn.setFont(self.ui.save_btn.font())

        # Create a button for removing a line
        self.remove_line_btn = QPushButton("Remove Line", self)
        self.remove_line_btn.setMinimumSize(115, 30)
        self.remove_line_btn.setFont(self.ui.save_btn.font())

        # Add buttons to the layout
        self.ui.btn_hbox.insertWidget(0, self.add_line_btn)
        self.ui.btn_hbox.insertWidget(1, self.remove_line_btn)

    def connect_signals_slots(self):
        """Connect signals and slots"""
        # Connect save button
        self.ui.save_btn.clicked.connect(self.save_invoice)

        # Connect add and remove line buttons
        self.add_line_btn.clicked.connect(self.add_invoice_line)
        self.remove_line_btn.clicked.connect(self.remove_invoice_line)

    def save_invoice(self):
        """Save the invoice changes"""
        if not self.invoice:
            return

        try:
            # Get data from form
            customer_id = self.ui.customer_cb.currentData()
            invoice_date = datetime.strptime(self.ui.invoice_date_edit.date().toString("yyyy-MM-dd"), "%Y-%m-%d").date()
            due_date = datetime.strptime(self.ui.due_date_edit.date().toString("yyyy-MM-dd"), "%Y-%m-%d").date()

            # Save all changes to invoice lines first
            self.invoice_lines_model.save_all_changes()

            # Refresh the invoice to get updated line items
            self.invoice = self.invoice_dao.get_invoice_with_lines(self.invoice_id)

            # Calculate totals based on line items
            subtotal = sum(line.subtotal for line in self.invoice.invoice_lines)
            tax_amount = sum(line.tax_amount for line in self.invoice.invoice_lines)
            total_amount = subtotal + tax_amount

            # Prepare data for update
            invoice_data = {
                'customer_id': customer_id,
                'date': invoice_date,
                'due_date': due_date,
                'subtotal': subtotal,
                'tax_amount': tax_amount,
                'total_amount': total_amount
            }

            # Update invoice
            updated_invoice = self.invoice_dao.update_invoice(self.invoice_id, invoice_data)

            if updated_invoice:
                QMessageBox.information(self, "Success", "Invoice updated successfully")
                # Close the form after successful update
                self.close()
            else:
                QMessageBox.warning(self, "Warning", "Failed to update invoice")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def add_invoice_line(self):
        """Add a new invoice line"""
        try:
            # Create a new invoice line with default values
            new_line = InvoiceLine(
                invoice_id=self.invoice_id,
                description="New Line Item",
                quantity=1.0,
                unit_price=0.0,
                tax_amount=0.0,
                subtotal=0.0,
                line_amount=0.0
            )

            # Add the line to the database
            added_line = self.invoice_dao.add_invoice_line(new_line)

            if added_line:
                # Reload the invoice lines
                self.invoice_lines_model.load_data()

                # Recalculate invoice totals
                self.invoice_dao.recalculate_invoice_totals(self.invoice_id)

                # Refresh the invoice object
                self.invoice = self.invoice_dao.get_invoice_with_lines(self.invoice_id)
            else:
                QMessageBox.warning(self, "Warning", "Failed to add invoice line")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def remove_invoice_line(self):
        """Remove the selected invoice line"""
        try:
            # Get the selected row
            selected_indexes = self.ui.invoice_lines_table_view.selectedIndexes()

            if not selected_indexes:
                QMessageBox.warning(self, "Warning", "Please select an invoice line to remove")
                return

            # Get the row of the first selected index
            row = selected_indexes[0].row()

            # Get the invoice line ID
            line_id = self.invoice_lines_model.invoice_lines[row].id

            # Confirm deletion
            reply = QMessageBox.question(
                self,
                "Confirm Deletion",
                "Are you sure you want to remove this invoice line?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # Delete the line
                deleted = self.invoice_dao.delete_invoice_line(line_id)

                if deleted:
                    # Reload the invoice lines
                    self.invoice_lines_model.load_data()

                    # Recalculate invoice totals
                    self.invoice_dao.recalculate_invoice_totals(self.invoice_id)

                    # Refresh the invoice object
                    self.invoice = self.invoice_dao.get_invoice_with_lines(self.invoice_id)
                else:
                    QMessageBox.warning(self, "Warning", "Failed to remove invoice line")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")