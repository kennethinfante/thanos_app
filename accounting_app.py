from PyQt5.QtWidgets import QMainWindow, QTabWidget
from customers import Customer
from vendors import Vendor
from invoices import Invoice
from bills import Bill
from utils.database import create_connection

class AccountingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Thanos Accounting"
        self.db_path = "accounting.db"
        self.conn = create_connection(self.db_path)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1000, 600)

        # Create tab widget
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Add modules
        self.customer_module = CustomerModule(self.conn)
        self.vendor_module = VendorModule(self.conn)
        self.invoice_module = InvoiceModule(self.conn)
        self.bill_module = BillModule(self.conn)

        # Add tabs
        self.tab_widget.addTab(self.customer_module, "Customers")
        self.tab_widget.addTab(self.vendor_module, "Vendors")
        self.tab_widget.addTab(self.invoice_module, "Invoices")
        self.tab_widget.addTab(self.bill_module, "Bills")

        self.show()