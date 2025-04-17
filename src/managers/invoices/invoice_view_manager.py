from PyQt5.QtWidgets import QMainWindow, QMessageBox, QPushButton
from PyQt5.QtCore import QDate
from datetime import datetime

from forms_py.invoice_view import Ui_invoiceView

from src.models.invoice_view_model import InvoiceViewModel
from src.models.invoice_view_delegate import InvoiceViewDelegate

from src.dao.invoice_dao import InvoiceDao
from src.dao.customer_dao import CustomerDao
# for adding or removing locally
from src.do.invoice import InvoiceLine

class InvoiceViewManager(QMainWindow):

    def __init__(self, invoice_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_invoiceView()
        self.ui.setupUi(self)

        self.invoice_id = invoice_id
        self.invoice_dao = InvoiceDao()
        self.customer_dao = CustomerDao()

        # Create the invoice lines model
        self.invoice_lines_model = InvoiceViewModel(invoice_id)

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

        # Initialize the total amount labels
        self.update_total_labels()


    def load_customers(self):
        """Load customers into the customer combobox"""
        self.ui.customer_cb.clear()
        customers = self.customer_dao.get_all_customers()

        for customer in customers:
            self.ui.customer_cb.addItem(customer.name, customer.id)

    def update_total_labels(self):
        """Update the subtotal, tax, and total amount labels based on current invoice lines"""
        try:
            # Calculate totals from the current invoice lines in the model
            subtotal = 0.0
            tax_amount = 0.0

            for line in self.invoice_lines_model.invoice_lines:
                # Calculate subtotal (quantity * unit_price)
                quantity = line.quantity if hasattr(line, 'quantity') and line.quantity is not None else 0
                unit_price = line.unit_price if hasattr(line, 'unit_price') and line.unit_price is not None else 0
                line_subtotal = quantity * unit_price

                # Get tax amount
                line_tax = line.tax_amount if hasattr(line, 'tax_amount') and line.tax_amount is not None else 0

                # Add to totals
                subtotal += line_subtotal
                tax_amount += line_tax

            # Calculate total
            total_amount = subtotal + tax_amount

            # Update the labels with formatted currency values
            self.ui.subtotal_amt_label.setText(f"${subtotal:.2f}")
            self.ui.tax_amt_label.setText(f"${tax_amount:.2f}")
            self.ui.total_amt_label.setText(f"${total_amount:.2f}")

        except Exception as e:
            print(f"Error updating total labels: {str(e)}")

    def load_invoice_lines(self):
        """Load invoice line items into the table view"""
        # Set the model for the invoice lines table view
        self.ui.invoice_lines_table_view.setModel(self.invoice_lines_model)

        # Create and configure the delegate
        delegate = InvoiceViewDelegate(self.ui.invoice_lines_table_view)
        delegate.set_items(self.invoice_lines_model.get_available_items())
        delegate.set_accounts(self.invoice_lines_model.get_available_accounts())
        delegate.set_tax_rates(self.invoice_lines_model.get_available_tax_rates())

        # Set the delegate for the table view
        self.ui.invoice_lines_table_view.setItemDelegate(delegate)

        # Adjust column widths for better display
        # ["Item", "Account", "Description", "Quantity", "Unit Price", "Tax", "Subtotal", "Tax Amount", "Line Amount"]
        self.ui.invoice_lines_table_view.setColumnWidth(0, 150)
        self.ui.invoice_lines_table_view.setColumnWidth(1, 150)
        self.ui.invoice_lines_table_view.setColumnWidth(2, 200)
        self.ui.invoice_lines_table_view.setColumnWidth(3, 100)
        self.ui.invoice_lines_table_view.setColumnWidth(4, 100)
        self.ui.invoice_lines_table_view.setColumnWidth(5, 100)
        self.ui.invoice_lines_table_view.setColumnWidth(6, 100)
        self.ui.invoice_lines_table_view.setColumnWidth(7, 100)
        self.ui.invoice_lines_table_view.setColumnWidth(8, 100)

        # Connect the totalsChanged signal to update the total labels
        self.invoice_lines_model.totalsChanged.connect(self.update_total_labels)

    def connect_signals_slots(self):
        """Connect signals and slots"""
        # Connect save button
        self.ui.save_btn.clicked.connect(self.save_invoice)
        self.ui.cancel_btn.clicked.connect(self.cancel_changes)

        # Connect add and remove line buttons
        self.ui.add_line_btn.clicked.connect(self.add_invoice_line)
        self.ui.remove_line_btn.clicked.connect(self.remove_invoice_line)

        # Delete
        self.ui.delete_btn.clicked.connect(self.delete_invoice)

    def save_invoice(self):
        """Save the invoice changes"""
        if not self.invoice:
            return

        try:
            # Get data from form
            customer_id = self.ui.customer_cb.currentData()
            invoice_date = datetime.strptime(self.ui.invoice_date_edit.date().toString("yyyy-MM-dd"), "%Y-%m-%d").date()
            due_date = datetime.strptime(self.ui.due_date_edit.date().toString("yyyy-MM-dd"), "%Y-%m-%d").date()

            # seems this part is not used
            # Get the current totals from our calculated values
            # subtotal_text = self.ui.subtotal_amt_label.text().replace('$', '')
            # tax_text = self.ui.tax_amt_label.text().replace('$', '')
            # total_text = self.ui.total_amt_label.text().replace('$', '')
            #
            # subtotal = float(subtotal_text)
            # tax_amount = float(tax_text)
            # total_amount = float(total_text)

             # Save all changes to invoice lines first
            try:
                self.invoice_lines_model.save_all_changes()
            except ValueError as ve:
                QMessageBox.warning(self, "Validation Error", str(ve))
                return

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

    def cancel_changes(self):
        """Cancel the changes and close the form"""
        # Ask for confirmation if there are unsaved changes
        if self.invoice_lines_model.has_unsaved_changes():
            reply = QMessageBox.question(
                self,
                "Confirm Cancel",
                "You have unsaved changes. Are you sure you want to cancel?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.No:
                return

        # Close the form without saving
        self.close()

    def delete_invoice(self):
        """Delete the current invoice"""
        if not self.invoice:
            return

        # Confirm deletion
        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            "Are you sure you want to delete this invoice? This action cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                # Delete the invoice
                deleted = self.invoice_dao.delete_invoice(self.invoice_id)

                if deleted:
                    QMessageBox.information(self, "Success", "Invoice deleted successfully")

                    # Close the form after successful deletion
                    self.close()
                else:
                    QMessageBox.warning(self, "Warning", "Failed to delete invoice")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def add_invoice_line(self):
        try:
            # Add a new line to the model
            added = self.invoice_lines_model.add_line_locally()

            if not added:
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

            # Confirm deletion
            reply = QMessageBox.question(
                self,
                "Confirm Deletion",
                "Are you sure you want to remove this invoice line?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # Remove the line locally
                removed = self.invoice_lines_model.remove_line_locally(row)

                if not removed:
                    QMessageBox.warning(self, "Warning", "Failed to remove invoice line")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")