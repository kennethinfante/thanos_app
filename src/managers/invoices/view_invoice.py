from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDate
from forms_python.invoice_view_edit import Ui_viewEditInvoice
from src.dao.invoice_dao import InvoiceDao
from src.dao.customer_dao import CustomerDao
from src.models.invoice_lines_model import InvoiceLinesModel

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
        self.ui.invoice_lines_table_view.setColumnWidth(0, 50)  # ID
        self.ui.invoice_lines_table_view.setColumnWidth(1, 300)  # Description
        self.ui.invoice_lines_table_view.setColumnWidth(2, 100)  # Quantity
        self.ui.invoice_lines_table_view.setColumnWidth(3, 100)  # Unit Price
        self.ui.invoice_lines_table_view.setColumnWidth(4, 100)  # Tax Rate
        self.ui.invoice_lines_table_view.setColumnWidth(5, 100)  # Tax Amount
        self.ui.invoice_lines_table_view.setColumnWidth(6, 100)  # Line Amount

    def connect_signals_slots(self):
        """Connect signals and slots"""
        # Connect save button
        self.ui.save_btn.clicked.connect(self.save_invoice)

    def save_invoice(self):
        """Save the invoice changes"""
        if not self.invoice:
            return

        # Get data from form
        customer_id = self.ui.customer_cb.currentData()
        invoice_date = self.ui.invoice_date_edit.date().toString("yyyy-MM-dd")
        due_date = self.ui.due_date_edit.date().toString("yyyy-MM-dd")

        # Prepare data for update
        invoice_data = {
            'customer_id': customer_id,
            'date': invoice_date,
            'due_date': due_date,
            # Add other fields as needed
        }

        # Update invoice
        updated_invoice = self.invoice_dao.update_invoice(self.invoice_id, invoice_data)

        if updated_invoice:
            # Close the form after successful update
            self.close()