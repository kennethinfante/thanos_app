## Recommended File Structure
1.main.py - Entry point and main application setup
2.accounting_app.py - Main application window class
3.customers/ - Customer-related functionality
customer_view.py - Customer list view and management
customer_dialogs.py - Customer creation/editing dialogs
4.vendors/ - Vendor-related functionality
vendor_view.py - Vendor list view and management
vendor_dialogs.py - Vendor creation/editing dialogs
5.invoices/ - Invoice-related functionality
invoice_view.py - Invoice list view
invoice_dialogs.py - Invoice creation/editing dialogs
6.bills/ - Bill-related functionality
bill_view.py - Bill list view
bill_dialogs.py - Bill creation/editing dialogs
7.utils/ - Utility functions and shared components
styles.py - Theme and styling
widgets.py - Custom widgets or shared UI components

## Implementation Example
Here's how you could implement this structure:

```py
# main.py
import sys
from PyQt5.QtWidgets import QApplication
from accounting_app import AccountingApp
from utils.styles import apply_dark_theme

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle("Fusion")
    
    # Apply dark theme
    apply_dark_theme(app)
    
    window = AccountingApp()
    window.show()
    
    sys.exit(app.exec_())


# accounting_app.py
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from customers.customer_view import CustomerView
from vendors.vendor_view import VendorView
from invoices.invoice_view import InvoiceView
from bills.bill_view import BillView

class AccountingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thanos Accounting")
        self.setMinimumSize(1200, 800)
        
        # Create tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Initialize tabs
        self.customer_view = CustomerView()
        self.vendor_view = VendorView()
        self.invoice_view = InvoiceView()
        self.bill_view = BillView()
        
        # Add tabs
        self.tabs.addTab(self.customer_view, "Customers")
        self.tabs.addTab(self.vendor_view, "Vendors")
        self.tabs.addTab(self.invoice_view, "Invoices")
        self.tabs.addTab(self.bill_view, "Bills")

# styles.py
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

def apply_dark_theme(app):
    """Apply dark theme to the application"""
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

# customer_view.py
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                            QTableWidget, QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import Qt
from .customer_dialogs import create_new_customer_dialog, view_customer_details_dialog

class CustomerView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_customers()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Buttons
        buttons_layout = QHBoxLayout()
        
        self.new_customer_btn = QPushButton("New Customer")
        self.new_customer_btn.clicked.connect(self.create_new_customer)
        buttons_layout.addWidget(self.new_customer_btn)
        
        buttons_layout.addStretch()
        
        layout.addLayout(buttons_layout)
        
        # Customers table
        self.customers_table = QTableWidget(0, 5)
        self.customers_table.setHorizontalHeaderLabels(["ID", "Name", "Email", "Phone", "Balance"])
        self.customers_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.customers_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.customers_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.customers_table.doubleClicked.connect(self.on_customer_double_clicked)
        
        layout.addWidget(self.customers_table)
    
    def load_customers(self):
        """Load customers from database (mock data for now)"""
        # Clear existing data
        self.customers_table.setRowCount(0)
        
        # Sample data
        sample_customers = [
            ["C001", "ABC Company", "contact@abc.com", "555-1234", "$3,500.00"],
            ["C002", "XYZ Corporation", "info@xyz.com", "555-5678", "$1,200.00"],
            ["C003", "Acme Inc.", "sales@acme.com", "555-9012", "$750.00"],
            ["C004", "Global Services", "info@globalservices.com", "555-3456", "$0.00"],
            ["C005", "Local Shop", "shop@local.com", "555-7890", "$250.00"]
        ]
        
        for i, customer in enumerate(sample_customers):
            self.customers_table.insertRow(i)
            for j, value in enumerate(customer):
                self.customers_table.setItem(i, j, QTableWidgetItem(value))
    
    def on_customer_double_clicked(self, index):
        """Handle double-click on customer row"""
        row = index.row()
        self.view_customer_details(row)
    
    def create_new_customer(self):
        """Create a new customer"""
        if create_new_customer_dialog(self):
            self.load_customers()  # Refresh the table
    
    def view_customer_details(self, row):
        """View customer details"""
        customer_id = self.customers_table.item(row, 0).text()
        customer_name = self.customers_table.item(row, 1).text()
        view_customer_details_dialog(self, row, customer_id, customer_name, self.customers_table)
```

You would implement similar structures for the other modules (vendors, invoices, bills).

## Benefits of This Structure
1. Modularity: Each component is isolated, making it easier to understand and maintain
2. Reusability: Common functions and widgets can be shared across modules
3. Scalability: New features can be added without modifying existing code
4. Testability: Each module can be tested independently
5. Collaboration: Multiple developers can work on different modules simultaneously

This structure follows the principle of separation of concerns, where each file has a specific responsibility, making the codebase more maintainable and easier to navigate.

## Additional Tips

If you decide to implement this structure, here are a few additional tips:
1. Create __init__.py files in each directory to make them proper Python packages
2. Consider adding a database module for handling data persistence
3. You might want to create a shared models directory for data structures used across modules
4. For larger forms, consider using Qt Designer and .ui files for layout design

Feel free to reach out if you need any further assistance with implementing specific parts of the application or if you have questions about PyQt5 functionality. Good luck with your Thanos Accounting project!

## Common Imports

```py
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
#                             QHBoxLayout, QPushButton, QLabel, QStackedWidget, 
#                             QTreeWidget, QTreeWidgetItem, QSplitter, QFrame, 
#                             QStatusBar, QAction, QToolBar, QMenu, QMessageBox,
#                             QDialog, QLineEdit, QFormLayout, QDateEdit, QComboBox,
#                             QTableWidget, QTableWidgetItem, QHeaderView, QTextEdit)

# from PyQt5.QtGui import QIcon, QFont, QPixmap, QPalette, QColor
# from PyQt5.QtCore import Qt, QSize, QDate
```


## Notes
Advantage of separate bill and invoice payments tables
* Easy getting AR and AP balance
* Easy getting payment reference numbers

Advantage of single cash table
* Easier for reconciliation

Products and services
* If tracked - is_sold and is_purchased are checked, COGS, Sales, Inventory
* If not tracked
    * if purchase but not sold - consumables
    * If sold but not purchase - service
    * If purchase and sold - inventory is purchases

## User Story for Products and services
Let: 
    is_inventory_tracked = 1
    is_consumable = 2
    is_service = 3

* If 1 is clicked
    * 2 and 3 are greyed out.
    * Inventory account is prepopulated, greyed out
    * Sales account is prepopulated, greyed out
    * COGS is prepopulated, greye out

* If 2 is clicked
    * 1 & 3 are greyed out.
    * Inventory is blank, greyed out
    * Sales account is blank, greyed out
    * Purchases - default to Supplies expense, editable

* If 3 is clicked
    * 2 & 1 are greyed out
    * Inventory is blank, greyed out
    * Sales - default to Service revenue, editable
    * Purchases - account is blank, editable. Note that if not blank, item name will be appended with "(purchased)"

* If none is clicked
    * Inventory is blank, greyed out
    * Sales - blank, editable
    * Purchases - blank, editable

Note that in bills, items without Expense accounts are not available. In invoices, items without revenue accounts are not available.