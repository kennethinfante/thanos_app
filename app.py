#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Accounting Software - Main Application
A desktop accounting application built with PyQt5
"""

import sys
import os
import sqlite3
from datetime import datetime
from random import random

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

# Database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

class AccountingApp(qtw.QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.title = "Accounting Software"
        self.db_path = "accounting.db"
        self.conn = create_connection(self.db_path)
        
        # Initialize UI
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1200, 800)
        
        # Set up the central widget and main layout
        self.central_widget = qtw.QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = qtw.QVBoxLayout(self.central_widget)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create status bar
        self.statusBar = qtw.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")
        
        # Create main content area with splitter
        self.splitter = qtw.QSplitter(qtc.Qt.Horizontal)
        self.main_layout.addWidget(self.splitter)
        
        # Create navigation panel
        self.nav_panel = self.create_navigation_panel()
        self.splitter.addWidget(self.nav_panel)
        
        # Create content area
        self.content_area = qtw.QStackedWidget()
        self.splitter.addWidget(self.content_area)
        
        # Set splitter sizes
        self.splitter.setSizes([250, 950])
        
        # Add dashboard as the default view
        self.dashboard_widget = self.create_dashboard()
        self.content_area.addWidget(self.dashboard_widget)
        
        # Add other content widgets
        self.chart_of_accounts_widget = self.create_chart_of_accounts()
        self.content_area.addWidget(self.chart_of_accounts_widget)
        
        self.journal_entries_widget = self.create_journal_entries()
        self.content_area.addWidget(self.journal_entries_widget)
        
        self.customers_widget = self.create_customers()
        self.content_area.addWidget(self.customers_widget)
        
        self.vendors_widget = self.create_vendors()
        self.content_area.addWidget(self.vendors_widget)
        
        self.reports_widget = self.create_reports()
        self.content_area.addWidget(self.reports_widget)
        
        # Show the application
        self.show()
        
    def create_menu_bar(self):
        """Create the application menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        new_company_action = qtw.QAction('New Company', self)
        new_company_action.setStatusTip('Create a new company')
        new_company_action.triggered.connect(self.new_company)
        file_menu.addAction(new_company_action)
        
        open_company_action = qtw.QAction('Open Company', self)
        open_company_action.setStatusTip('Open an existing company')
        open_company_action.triggered.connect(self.open_company)
        file_menu.addAction(open_company_action)
        
        file_menu.addSeparator()
        
        backup_action = qtw.QAction('Backup Company', self)
        backup_action.setStatusTip('Backup company data')
        backup_action.triggered.connect(self.backup_company)
        file_menu.addAction(backup_action)
        
        file_menu.addSeparator()
        
        exit_action = qtw.QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu('Edit')
        
        preferences_action = qtw.QAction('Preferences', self)
        preferences_action.setStatusTip('Edit application preferences')
        preferences_action.triggered.connect(self.edit_preferences)
        edit_menu.addAction(preferences_action)
        
        # View menu
        view_menu = menubar.addMenu('View')
        
        # Reports menu
        reports_menu = menubar.addMenu('Reports')
        
        income_statement_action = qtw.QAction('Income Statement', self)
        income_statement_action.triggered.connect(self.show_income_statement)
        reports_menu.addAction(income_statement_action)
        
        balance_sheet_action = qtw.QAction('Balance Sheet', self)
        balance_sheet_action.triggered.connect(self.show_balance_sheet)
        reports_menu.addAction(balance_sheet_action)
        
        cash_flow_action = qtw.QAction('Cash Flow Statement', self)
        cash_flow_action.triggered.connect(self.show_cash_flow)
        reports_menu.addAction(cash_flow_action)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        
        about_action = qtw.QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def create_toolbar(self):
        """Create the main toolbar"""
        self.toolbar = qtw.QToolBar("Main Toolbar")
        self.toolbar.setIconSize(qtc.QSize(32, 32))
        self.addToolBar(self.toolbar)
        
        # Add actions to toolbar
        dashboard_action = qtw.QAction(qtg.QIcon("icons/dashboard.png"), "Dashboard", self)
        dashboard_action.triggered.connect(lambda: self.content_area.setCurrentWidget(self.dashboard_widget))
        self.toolbar.addAction(dashboard_action)
        
        customers_action = qtw.QAction(qtg.QIcon("icons/customers.png"), "Customers", self)
        customers_action.triggered.connect(lambda: self.content_area.setCurrentWidget(self.customers_widget))
        self.toolbar.addAction(customers_action)
        
        vendors_action = qtw.QAction(qtg.QIcon("icons/vendors.png"), "Vendors", self)
        vendors_action.triggered.connect(lambda: self.content_area.setCurrentWidget(self.vendors_widget))
        self.toolbar.addAction(vendors_action)
        
        journal_action = qtw.QAction(qtg.QIcon("icons/journal.png"), "Journal Entries", self)
        journal_action.triggered.connect(lambda: self.content_area.setCurrentWidget(self.journal_entries_widget))
        self.toolbar.addAction(journal_action)
        
        reports_action = qtw.QAction(qtg.QIcon("icons/reports.png"), "Reports", self)
        reports_action.triggered.connect(lambda: self.content_area.setCurrentWidget(self.reports_widget))
        self.toolbar.addAction(reports_action)
        
    def create_navigation_panel(self):
        """Create the navigation panel"""
        nav_widget = qtw.QWidget()
        nav_layout = qtw.QVBoxLayout(nav_widget)
        
        # Company name label
        company_label = qtw.QLabel("Your Company Name")
        company_label.setFont(qtg.QFont("Arial", 14, qtg.QFont.Bold))
        nav_layout.addWidget(company_label)
        
        # Navigation tree
        self.nav_tree = qtw.QTreeWidget()
        self.nav_tree.setHeaderHidden(True)
        nav_layout.addWidget(self.nav_tree)
        
        # Add navigation items
        # Banking
        banking_item = qtw.QTreeWidgetItem(["Banking"])
        banking_item.addChild(qtw.QTreeWidgetItem(["Bank Accounts"]))
        banking_item.addChild(qtw.QTreeWidgetItem(["Write Checks"]))
        banking_item.addChild(qtw.QTreeWidgetItem(["Reconcile"]))
        self.nav_tree.addTopLevelItem(banking_item)
        
        # Sales
        sales_item = qtw.QTreeWidgetItem(["Sales"])
        sales_item.addChild(qtw.QTreeWidgetItem(["Customers"]))
        sales_item.addChild(qtw.QTreeWidgetItem(["Invoices"]))
        sales_item.addChild(qtw.QTreeWidgetItem(["Receive Payments"]))
        self.nav_tree.addTopLevelItem(sales_item)
        
        # Expenses
        expenses_item = qtw.QTreeWidgetItem(["Expenses"])
        expenses_item.addChild(qtw.QTreeWidgetItem(["Vendors"]))
        expenses_item.addChild(qtw.QTreeWidgetItem(["Bills"]))
        expenses_item.addChild(qtw.QTreeWidgetItem(["Pay Bills"]))
        self.nav_tree.addTopLevelItem(expenses_item)
        
        # Accounting
        accounting_item = qtw.QTreeWidgetItem(["Accounting"])
        accounting_item.addChild(qtw.QTreeWidgetItem(["Chart of Accounts"]))
        accounting_item.addChild(qtw.QTreeWidgetItem(["Journal Entries"]))
        self.nav_tree.addTopLevelItem(accounting_item)
        
        # Reports
        reports_item = qtw.QTreeWidgetItem(["Reports"])
        reports_item.addChild(qtw.QTreeWidgetItem(["Income Statement"]))
        reports_item.addChild(qtw.QTreeWidgetItem(["Balance Sheet"]))
        reports_item.addChild(qtw.QTreeWidgetItem(["Cash Flow"]))
        reports_item.addChild(qtw.QTreeWidgetItem(["Tax Reports"]))
        self.nav_tree.addTopLevelItem(reports_item)
        
        # Connect tree item clicks to actions
        self.nav_tree.itemClicked.connect(self.handle_navigation)
        
        return nav_widget
    
    def handle_navigation(self, item, column):
        """Handle navigation tree item clicks"""
        if item.text(0) == "Chart of Accounts":
            self.content_area.setCurrentWidget(self.chart_of_accounts_widget)
        elif item.text(0) == "Journal Entries":
            self.content_area.setCurrentWidget(self.journal_entries_widget)
        elif item.text(0) == "Customers":
            self.content_area.setCurrentWidget(self.customers_widget)
        elif item.text(0) == "Vendors":
            self.content_area.setCurrentWidget(self.vendors_widget)
        elif item.text(0) == "Income Statement":
            self.show_income_statement()
        elif item.text(0) == "Balance Sheet":
            self.show_balance_sheet()
        elif item.text(0) == "Cash Flow":
            self.show_cash_flow()
    
    def create_dashboard(self):
        """Create the dashboard widget"""
        dashboard = qtw.QWidget()
        layout = qtw.QVBoxLayout(dashboard)
        
        # Welcome header
        header_layout = qtw.QHBoxLayout()qtw.
        layout.addLayout(header_layout)
        
        welcome_label = qtw.QLabel("Welcome to Your Accounting Software")
        welcome_label.setFont(qtg.QFont("Arial", 18, qtg.QFont.Bold))
        header_layout.addWidget(welcome_label)
        header_layout.addStretch()
        
        date_label = qtw.QLabel(f"Today: {datetime.now().strftime('%B %d, %Y')}")
        date_label.setFont(qtg.QFont("Arial", 12))
        header_layout.addWidget(date_label)
        
        # Add horizontal line
        line = qtw.QFrame()
        line.setFrameShape(qtw.QFrame.HLine)
        line.setFrameShadow(qtw.QFrame.Sunken)
        layout.addWidget(line)
        
        # Dashboard content
        content_layout = qtw.QHBoxLayout()
        layout.addLayout(content_layout)
        
        # Left column - Financial summary
        left_column = qtw.QVBoxLayout()
        content_layout.addLayout(left_column)
        
        financial_summary = qtw.QLabel("Financial Summary")
        financial_summary.setFont(qtg.QFont("Arial", 14, qtg.QFont.Bold))
        left_column.addWidget(financial_summary)
        
        # Financial metrics
        metrics_layout = qtw.QFormLayout()
        left_column.addLayout(metrics_layout)
        
        # These would be populated from the database in a real app
        metrics_layout.addRow("Total Revenue:", qtw.QLabel("$125,000.00"))
        metrics_layout.addRow("Total Expenses:", qtw.QLabel("$85,000.00"))
        metrics_layout.addRow("Net Income:", qtw.QLabel("$40,000.00"))
        metrics_layout.addRow("Cash Balance:", qtw.QLabel("$65,000.00"))
        metrics_layout.addRow("Accounts Receivable:", qtw.QLabel("$32,000.00"))
        metrics_layout.addRow("Accounts Payable:", qtw.QLabel("$18,000.00"))
        
        left_column.addStretch()
        
        # Middle column - Recent transactions
        middle_column = qtw.QVBoxLayout()
        content_layout.addLayout(middle_column)
        
        recent_transactions = qtw.QLabel("Recent Transactions")
        recent_transactions.setFont(qtg.QFont("Arial", 14, qtg.QFont.Bold))
        middle_column.addWidget(recent_transactions)
        
        # Transactions table
        transactions_table = qtw.QTableWidget(5, 4)
        transactions_table.setHorizontalHeaderLabels(["Date", "Description", "Account", "Amount"])
        transactions_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        middle_column.addWidget(transactions_table)
        
        # Sample data - would come from database in real app
        sample_transactions = [
            ["2023-05-01", "Office Supplies", "Expenses", "$250.00"],
            ["2023-05-03", "Client Payment", "Revenue", "$1,500.00"],
            ["2023-05-05", "Rent Payment", "Expenses", "$2,000.00"],
            ["2023-05-10", "Consulting Services", "Revenue", "$3,500.00"],
            ["2023-05-15", "Utility Bill", "Expenses", "$175.00"]
        ]
        
        for row, transaction in enumerate(sample_transactions):
            for col, value in enumerate(transaction):
                item = qtw.QTableWidgetItem(value)
                transactions_table.setItem(row, col, item)
        
        view_all_btn = qtw.QPushButton("View All Transactions")
        view_all_btn.clicked.connect(self.view_all_transactions)
        middle_column.addWidget(view_all_btn)
        
        # Right column - Quick actions
        right_column = qtw.QVBoxLayout()
        content_layout.addLayout(right_column)
        
        quick_actions = qtw.QLabel("Quick Actions")
        quick_actions.setFont(qtg.QFont("Arial", 14, qtg.QFont.Bold))
        right_column.addWidget(quick_actions)
        
        # Action buttons
        new_invoice_btn = qtw.QPushButton("Create New Invoice")
        new_invoice_btn.clicked.connect(self.create_new_invoice)
        right_column.addWidget(new_invoice_btn)
        
        new_bill_btn = qtw.QPushButton("Enter New Bill")
        new_bill_btn.clicked.connect(self.enter_new_bill)
        right_column.addWidget(new_bill_btn)
        
        new_journal_btn = qtw.QPushButton("New Journal Entry")
        new_journal_btn.clicked.connect(self.create_journal_entry)
        right_column.addWidget(new_journal_btn)
        
        reconcile_btn = qtw.QPushButton("Reconcile Accounts")
        reconcile_btn.clicked.connect(self.reconcile_accounts)
        right_column.addWidget(reconcile_btn)
        
        run_report_btn = qtw.QPushButton("Run Reports")
        run_report_btn.clicked.connect(lambda: self.content_area.setCurrentWidget(self.reports_widget))
        right_column.addWidget(run_report_btn)
        
        right_column.addStretch()
        
        # Set column stretch factors
        content_layout.setStretch(0, 1)  # Left column
        content_layout.setStretch(1, 2)  # Middle column
        content_layout.setStretch(2, 1)  # Right column
        
        return dashboard
    
    def create_chart_of_accounts(self):
        """Create the chart of accounts widget"""
        widget = qtw.QWidget()
        layout = qtw.QVBoxLayout(widget)
        
        # Header
        header_layout = qtw.QHBoxLayout()
        layout.addLayout(header_layout)
        
        title = qtw.QLabel("Chart of Accounts")
        title.setFont(qtg.QFont("Arial", 16, qtg.QFont.Bold))
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        new_account_btn = qtw.QPushButton("New Account")
        new_account_btn.clicked.connect(self.create_new_account)
        header_layout.addWidget(new_account_btn)
        
        # Table of accounts
        self.accounts_table = qtw.QTableWidget()
        self.accounts_table.setColumnCount(5)
        self.accounts_table.setHorizontalHeaderLabels(["Account #", "Account Name", "Type", "Balance", "Actions"])
        self.accounts_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.accounts_table.horizontalHeader().setSectionResizeMode(4, qtw.QHeaderView.ResizeToContents)
        layout.addWidget(self.accounts_table)
        
        # Load accounts from database
        self.load_chart_of_accounts()
        
        return widget
    
    def load_chart_of_accounts(self):
        """Load chart of accounts from database"""
        # In a real app, this would fetch from the database
        # For now, we'll use sample data
        sample_accounts = [
            ["1000", "Cash", "Asset", "$25,000.00"],
            ["1100", "Accounts Receivable", "Asset", "$32,000.00"],
            ["1200", "Inventory", "Asset", "$45,000.00"],
            ["1500", "Office Equipment", "Asset", "$15,000.00"],
            ["2000", "Accounts Payable", "Liability", "$18,000.00"],
            ["2100", "Loans Payable", "Liability", "$50,000.00"],
            ["3000", "Common Stock", "Equity", "$10,000.00"],
            ["3100", "Retained Earnings", "Equity", "$39,000.00"],
            ["4000", "Sales Revenue", "Revenue", "$125,000.00"],
            ["5000", "Cost of Goods Sold", "Expense", "$65,000.00"],
            ["6000", "Rent Expense", "Expense", "$12,000.00"],
            ["6100", "Utilities Expense", "Expense", "$8,000.00"]
        ]
        
        self.accounts_table.setRowCount(len(sample_accounts))
        
        for row, account in enumerate(sample_accounts):
            for col, value in enumerate(account):
                item = qtw.QTableWidgetItem(value)
                self.accounts_table.setItem(row, col, item)
            
            # Add action buttons
            actions_widget = qtw.QWidget()
            actions_layout = qtw.QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(0, 0, 0, 0)
            
            edit_btn = qtw.QPushButton("Edit")
            edit_btn.clicked.connect(lambda checked, r=row: self.edit_account(r))
            actions_layout.addWidget(edit_btn)
            
            view_btn = qtw.QPushButton("View")
            view_btn.clicked.connect(lambda checked, r=row: self.view_account_details(r))
            actions_layout.addWidget(view_btn)
            
            self.accounts_table.setCellWidget(row, 4, actions_widget)
    
    def create_journal_entries(self):
        """Create the journal entries widget"""
        widget = qtw.QWidget()
        layout = qtw.QVBoxLayout(widget)
        
        # Header
        header_layout = qtw.QHBoxLayout()
        layout.addLayout(header_layout)
        
        title = qtw.QLabel("Journal Entries")
        title.setFont(qtw.QFont("Arial", 16, qtw.QFont.Bold))
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        new_entry_btn = qtw.QPushButton("New Journal Entry")
        new_entry_btn.clicked.connect(self.create_journal_entry)
        header_layout.addWidget(new_entry_btn)
        
        # Journal entries table
        self.journal_table = qtw.QTableWidget()
        self.journal_table.setColumnCount(5)
        self.journal_table.setHorizontalHeaderLabels(["Date", "Reference", "Description", "Amount", "Actions"])
        self.journal_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.journal_table.horizontalHeader().setSectionResizeMode(4, qtw.QHeaderView.ResizeToContents)
        layout.addWidget(self.journal_table)
        
        # Load journal entries
        self.load_journal_entries()
        
        return widget
    
    def load_journal_entries(self):
        """Load journal entries from database"""
        # Sample data for now
        sample_entries = [
            ["2023-05-01", "JE001", "Initial investment", "$10,000.00"],
            ["2023-05-03", "JE002", "Purchase of equipment", "$5,000.00"],
            ["2023-05-05", "JE003", "Client payment", "$1,500.00"],
            ["2023-05-10", "JE004", "Rent payment", "$2,000.00"],
            ["2023-05-15", "JE005", "Utility payment", "$175.00"]
        ]
        
        self.journal_table.setRowCount(len(sample_entries))
        
        for row, entry in enumerate(sample_entries):
            for col, value in enumerate(entry):
                item = qtw.QTableWidgetItem(value)
                self.journal_table.setItem(row, col, item)
            
            # Add action buttons
            actions_widget = qtw.QWidget()
            actions_layout = qtw.QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(0, 0, 0, 0)
            
            edit_btn = qtw.QPushButton("Edit")
            edit_btn.clicked.connect(lambda checked, r=row: self.edit_journal_entry(r))
            actions_layout.addWidget(edit_btn)
            
            view_btn = qtw.QPushButton("View")
            view_btn.clicked.connect(lambda checked, r=row: self.view_journal_details(r))
            actions_layout.addWidget(view_btn)
            
            self.journal_table.setCellWidget(row, 4, actions_widget)
    
    def create_customers(self):
        """Create the customers widget"""
        widget = qtw.QWidget()
        layout = qtw.QVBoxLayout(widget)
        
        # Header
        header_layout = qtw.QHBoxLayout()
        layout.addLayout(header_layout)
        
        title = qtw.QLabel("Customers")
        title.setFont(qtg.QFont("Arial", 16, qtg.QFont.Bold))
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        # Search box
        search_layout = qtw.QHBoxLayout()
        search_layout.addWidget(qtw.QLabel("Search:"))
        search_input = qtw.QLineEdit()
        search_input.setPlaceholderText("Search customers...")
        search_input.textChanged.connect(self.search_customers)
        search_layout.addWidget(search_input)
        header_layout.addLayout(search_layout)
        
        new_customer_btn = qtw.QPushButton("New Customer")
        new_customer_btn.clicked.connect(self.create_new_customer)
        header_layout.addWidget(new_customer_btn)
        
        # Customers table
        self.customers_table = qtw.QTableWidget()
        self.customers_table.setColumnCount(6)
        self.customers_table.setHorizontalHeaderLabels(["ID", "Name", "Email", "Phone", "Balance", "Actions"])
        self.customers_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.customers_table.horizontalHeader().setSectionResizeMode(5, qtw.QHeaderView.ResizeToContents)
        layout.addWidget(self.customers_table)
        
        # Load customers
        self.load_customers()
        
        return widget
    
    def load_customers(self):
        """Load customers from database"""
        # Sample data for now
        sample_customers = [
            ["C001", "Acme Corporation", "contact@acme.com", "555-123-4567", "$5,200.00"],
            ["C002", "TechStart Inc.", "info@techstart.com", "555-234-5678", "$3,500.00"],
            ["C003", "Global Services LLC", "support@globalservices.com", "555-345-6789", "$12,000.00"],
            ["C004", "Local Business Co.", "hello@localbusiness.com", "555-456-7890", "$800.00"],
            ["C005", "Enterprise Solutions", "sales@enterprise.com", "555-567-8901", "$10,500.00"]
        ]
        
        self.customers_table.setRowCount(len(sample_customers))
        
        for row, customer in enumerate(sample_customers):
            for col, value in enumerate(customer):
                item = qtw.QTableWidgetItem(value)
                self.customers_table.setItem(row, col, item)
            
            # Add action buttons
            actions_widget = qtw.QWidget()
            actions_layout = qtw.QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(0, 0, 0, 0)
            
            edit_btn = qtw.QPushButton("Edit")
            edit_btn.clicked.connect(lambda checked, r=row: self.edit_customer(r))
            actions_layout.addWidget(edit_btn)
            
            view_btn = qtw.QPushButton("View")
            view_btn.clicked.connect(lambda checked, r=row: self.view_customer_details(r))
            actions_layout.addWidget(view_btn)
            
            invoice_btn = qtw.QPushButton("Invoice")
            invoice_btn.clicked.connect(lambda checked, r=row: self.create_invoice_for_customer(r))
            actions_layout.addWidget(invoice_btn)
            
            self.customers_table.setCellWidget(row, 5, actions_widget)
    
    def create_vendors(self):
        """Create the vendors widget"""
        widget = qtw.QWidget()
        layout = qtw.QVBoxLayout(widget)
        
        # Header
        header_layout = qtw.QHBoxLayout()
        layout.addLayout(header_layout)
        
        title = qtw.QLabel("Vendors")
        title.setFont(qtg.QFont("Arial", 16, qtg.QFont.Bold))
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        # Search box
        search_layout = qtw.QHBoxLayout()
        search_layout.addWidget(qtw.QLabel("Search:"))
        search_input = qtw.QLineEdit()
        search_input.setPlaceholderText("Search vendors...")
        search_input.textChanged.connect(self.search_vendors)
        search_layout.addWidget(search_input)
        header_layout.addLayout(search_layout)
        
        new_vendor_btn = qtw.QPushButton("New Vendor")
        new_vendor_btn.clicked.connect(self.create_new_vendor)
        header_layout.addWidget(new_vendor_btn)
        
        # Vendors table
        self.vendors_table = qtw.QTableWidget()
        self.vendors_table.setColumnCount(6)
        self.vendors_table.setHorizontalHeaderLabels(["ID", "Name", "Email", "Phone", "Balance", "Actions"])
        self.vendors_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.vendors_table.horizontalHeader().setSectionResizeMode(5, qtw.QHeaderView.ResizeToContents)
        layout.addWidget(self.vendors_table)
        
        # Load vendors
        self.load_vendors()
        
        return widget
    
    def load_vendors(self):
        """Load vendors from database"""
        # Sample data for now
        sample_vendors = [
            ["V001", "Office Supplies Co.", "orders@officesupplies.com", "555-111-2222", "$1,200.00"],
            ["V002", "Tech Hardware Inc.", "sales@techhardware.com", "555-222-3333", "$3,800.00"],
            ["V003", "Utility Services", "billing@utilityservices.com", "555-333-4444", "$750.00"],
            ["V004", "Maintenance Pros", "service@maintenancepros.com", "555-444-5555", "$500.00"],
            ["V005", "Marketing Agency", "contact@marketingagency.com", "555-555-6666", "$4,500.00"]
        ]
        
        self.vendors_table.setRowCount(len(sample_vendors))
        
        for row, vendor in enumerate(sample_vendors):
            for col, value in enumerate(vendor):
                item = qtw.QTableWidgetItem(value)
                self.vendors_table.setItem(row, col, item)
            
            # Add action buttons
            actions_widget = qtw.QWidget()
            actions_layout = qtw.QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(0, 0, 0, 0)
            
            edit_btn = qtw.QPushButton("Edit")
            edit_btn.clicked.connect(lambda checked, r=row: self.edit_vendor(r))
            actions_layout.addWidget(edit_btn)
            
            view_btn = qtw.QPushButton("View")
            view_btn.clicked.connect(lambda checked, r=row: self.view_vendor_details(r))
            actions_layout.addWidget(view_btn)
            
            bill_btn = qtw.QPushButton("Enter Bill")
            bill_btn.clicked.connect(lambda checked, r=row: self.create_bill_for_vendor(r))
            actions_layout.addWidget(bill_btn)
            
            self.vendors_table.setCellWidget(row, 5, actions_widget)
    
    def create_reports(self):
        """Create the reports widget"""
        widget = qtw.QWidget()
        layout = qtw.QVBoxLayout(widget)
        
        # Header
        title = qtw.QLabel("Financial Reports")
        title.setFont(qtg.QFont("Arial", 16, qtg.QFont.Bold))
        layout.addWidget(title)
        
        # Reports grid
        reports_grid = qtw.QGridLayout()
        layout.addLayout(reports_grid)
        
        # Financial statements
        financial_group = qtw.QGroupBox("Financial Statements")
        financial_layout = qtw.QVBoxLayout(financial_group)
        
        income_btn = qtw.QPushButton("Income Statement")
        income_btn.clicked.connect(self.show_income_statement)
        financial_layout.addWidget(income_btn)
        
        balance_btn = qtw.QPushButton("Balance Sheet")
        balance_btn.clicked.connect(self.show_balance_sheet)
        financial_layout.addWidget(balance_btn)
        
        cash_flow_btn = qtw.QPushButton("Cash Flow Statement")
        cash_flow_btn.clicked.connect(self.show_cash_flow)
        financial_layout.addWidget(cash_flow_btn)
        
        reports_grid.addWidget(financial_group, 0, 0)
        
        # Tax reports
        tax_group = qtw.QGroupBox("Tax Reports")
        tax_layout = qtw.QVBoxLayout(tax_group)
        
        sales_tax_btn = qtw.QPushButton("Sales Tax Report")
        sales_tax_btn.clicked.connect(self.show_sales_tax_report)
        tax_layout.addWidget(sales_tax_btn)
        
        payroll_tax_btn = qtw.QPushButton("Payroll Tax Report")
        payroll_tax_btn.clicked.connect(self.show_payroll_tax_report)
        tax_layout.addWidget(payroll_tax_btn)
        
        reports_grid.addWidget(tax_group, 0, 1)
        
        # Customer reports
        customer_group = qtw.QGroupBox("Customer Reports")
        customer_layout = qtw.QVBoxLayout(customer_group)
        
        ar_aging_btn = qtw.QPushButton("A/R Aging Report")
        ar_aging_btn.clicked.connect(self.show_ar_aging)
        customer_layout.addWidget(ar_aging_btn)
        
        customer_balance_btn = qtw.QPushButton("Customer Balances")
        customer_balance_btn.clicked.connect(self.show_customer_balances)
        customer_layout.addWidget(customer_balance_btn)
        
        sales_by_customer_btn = qtw.QPushButton("Sales by Customer")
        sales_by_customer_btn.clicked.connect(self.show_sales_by_customer)
        customer_layout.addWidget(sales_by_customer_btn)
        
        reports_grid.addWidget(customer_group, 1, 0)
        
        # Vendor reports
        vendor_group = qtw.QGroupBox("Vendor Reports")
        vendor_layout = qtw.QVBoxLayout(vendor_group)
        
        ap_aging_btn = qtw.QPushButton("A/P Aging Report")
        ap_aging_btn.clicked.connect(self.show_ap_aging)
        vendor_layout.addWidget(ap_aging_btn)
        
        vendor_balance_btn = qtw.QPushButton("Vendor Balances")
        vendor_balance_btn.clicked.connect(self.show_vendor_balances)
        vendor_layout.addWidget(vendor_balance_btn)
        
        purchases_by_vendor_btn = qtw.QPushButton("Purchases by Vendor")
        purchases_by_vendor_btn.clicked.connect(self.show_purchases_by_vendor)
        vendor_layout.addWidget(purchases_by_vendor_btn)
        
        reports_grid.addWidget(vendor_group, 1, 1)
        
        # Custom report section
        custom_group = qtw.QGroupBox("Custom Reports")
        custom_layout = qtw.QVBoxLayout(custom_group)
        
        date_range_layout = qtw.QHBoxLayout()
        date_range_layout.addWidget(qtw.QLabel("Date Range:"))
        
        self.start_date = qtw.QDateEdit(qtc.QDate.currentDate().addMonths(-1))
        date_range_layout.addWidget(self.start_date)
        
        date_range_layout.addWidget(qtw.QLabel("to"))
        
        self.end_date = qtw.QDateEdit(qtc.QDate.currentDate())
        date_range_layout.addWidget(self.end_date)
        
        custom_layout.addLayout(date_range_layout)
        
        report_type_layout = qtw.QHBoxLayout()
        report_type_layout.addWidget(qtw.QLabel("Report Type:"))
        
        self.report_type_combo = qtw.QComboBox()
        self.report_type_combo.addItems([
            "Income Statement", 
            "Balance Sheet", 
            "Cash Flow", 
            "Sales by Customer", 
            "Purchases by Vendor"
        ])
        report_type_layout.addWidget(self.report_type_combo)
        
        custom_layout.addLayout(report_type_layout)
        
        generate_btn = qtw.QPushButton("Generate Custom Report")
        generate_btn.clicked.connect(self.generate_custom_report)
        custom_layout.addWidget(generate_btn)
        
        reports_grid.addWidget(custom_group, 2, 0, 1, 2)
        
        layout.addStretch()
        
        return widget
    
    # Action methods
    def create_new_account(self):
        """Create a new account"""
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle("Create New Account")
        dialog.setMinimumWidth(400)
        
        layout = qtw.QVBoxLayout(dialog)
        
        form_layout = qtw.QFormLayout()
        
        account_number = qtw.QLineEdit()
        form_layout.addRow("Account Number:", account_number)
        
        account_name = qtw.QLineEdit()
        form_layout.addRow("Account Name:", account_name)
        
        account_type = qtw.QComboBox()
        account_type.addItems(["Asset", "Liability", "Equity", "Revenue", "Expense"])
        form_layout.addRow("Account Type:", account_type)
        
        description = qtw.QTextEdit()
        form_layout.addRow("Description:", description)
        
        layout.addLayout(form_layout)
        
        buttons = qtw.QDialogButtonBox(qtw.QDialogButtonBox.Ok | qtw.QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        if dialog.exec_() == qtw.QDialog.Accepted:
            # In a real app, save to database
            qtw.QMessageBox.information(self, "Success", "Account created successfully!")
            self.load_chart_of_accounts()  # Refresh the table
    
    def edit_account(self, row):
        """Edit an account"""
        account_number = self.accounts_table.item(row, 0).text()
        account_name = self.accounts_table.item(row, 1).text()
        
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle(f"Edit Account: {account_name}")
        dialog.setMinimumWidth(400)
        
        layout = qtw.QVBoxLayout(dialog)
        
        form_layout = qtw.QFormLayout()
        
        account_number_field = qtw.QLineEdit(account_number)
        form_layout.addRow("Account Number:", account_number_field)
        
        account_name_field = qtw.QLineEdit(account_name)
        form_layout.addRow("Account Name:", account_name_field)
        
        account_type = qtw.QComboBox()
        account_type.addItems(["Asset", "Liability", "Equity", "Revenue", "Expense"])
        account_type.setCurrentText(self.accounts_table.item(row, 2).text())
        form_layout.addRow("Account Type:", account_type)
        
        description = qtw.QTextEdit()
        form_layout.addRow("Description:", description)
        
        layout.addLayout(form_layout)
        
        buttons = qtw.QDialogButtonBox(qtw.QDialogButtonBox.Ok | qtw.QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        if dialog.exec_() == qtw.QDialog.Accepted:
            # In a real app, update in database
            qtw.QMessageBox.information(self, "Success", "Account updated successfully!")
            self.load_chart_of_accounts()  # Refresh the table
    
    def view_account_details(self, row):
        """View account details"""
        account_number = self.accounts_table.item(row, 0).text()
        account_name = self.accounts_table.item(row, 1).text()
        
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle(f"Account Details: {account_name}")
        dialog.setMinimumSize(600, 400)
        
        layout = qtw.QVBoxLayout(dialog)
        
        # Account info
        info_group = qtw.QGroupBox("Account Information")
        info_layout = qtw.QFormLayout(info_group)
        
        info_layout.addRow("Account Number:", qtw.QLabel(account_number))
        info_layout.addRow("Account Name:", qtw.QLabel(account_name))
        info_layout.addRow("Account Type:", qtw.QLabel(self.accounts_table.item(row, 2).text()))
        info_layout.addRow("Current Balance:", qtw.QLabel(self.accounts_table.item(row, 3).text()))
        
        layout.addWidget(info_group)
        
        # Transaction history
        history_group = qtw.QGroupBox("Transaction History")
        history_layout = qtw.QVBoxLayout(history_group)
        
        transactions_table = qtw.QTableWidget(5, 4)
        transactions_table.setHorizontalHeaderLabels(["Date", "Description", "Debit", "Credit"])
        transactions_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        
        # Sample data - would come from database in real app
        sample_transactions = [
            ["2023-05-01", "Initial balance", "$0.00", "$10,000.00"],
            ["2023-05-03", "Purchase of equipment", "$5,000.00", "$0.00"],
            ["2023-05-05", "Client payment", "$0.00", "$1,500.00"],
            ["2023-05-10", "Rent payment", "$2,000.00", "$0.00"],
            ["2023-05-15", "Utility payment", "$175.00", "$0.00"]
        ]
        
        for row, transaction in enumerate(sample_transactions):
            for col, value in enumerate(transaction):
                item = qtw.QTableWidgetItem(value)
                transactions_table.setItem(row, col, item)
        
        history_layout.addWidget(transactions_table)
        layout.addWidget(history_group)
        
        # Close button
        close_btn = qtw.QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        layout.addWidget(close_btn)
        
        dialog.exec_()
    
    def create_journal_entry(self):
        """Create a new journal entry"""
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle("Create Journal Entry")
        dialog.setMinimumSize(700, 500)
        
        layout = qtw.QVBoxLayout(dialog)
        
        # Header info
        header_layout = qtw.QFormLayout()
        
        date_edit = qtw.QDateEdit(qtc.QDate.currentDate())
        header_layout.addRow("Date:", date_edit)
        
        reference = qtw.QLineEdit()
        reference.setPlaceholderText("e.g., JE006")
        header_layout.addRow("Reference:", reference)
        
        description = qtw.QLineEdit()
        description.setPlaceholderText("Brief description of this entry")
        header_layout.addRow("Description:", description)
        
        layout.addLayout(header_layout)
        
        # Line items
        line_items_group = qtw.QGroupBox("Journal Entry Lines")
        line_items_layout = qtw.QVBoxLayout(line_items_group)
        
        line_items_table = qtw.QTableWidget(0, 4)
        line_items_table.setHorizontalHeaderLabels(["Account", "Description", "Debit", "Credit"])
        line_items_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        
        line_items_layout.addWidget(line_items_table)
        
        # Add line buttons
        buttons_layout = qtw.QHBoxLayout()
        
        add_line_btn = qtw.QPushButton("Add Line")
        add_line_btn.clicked.connect(lambda: self.add_journal_line(line_items_table))
        buttons_layout.addWidget(add_line_btn)
        
        remove_line_btn = qtw.QPushButton("Remove Line")
        remove_line_btn.clicked.connect(lambda: self.remove_journal_line(line_items_table))
        buttons_layout.addWidget(remove_line_btn)
        
        line_items_layout.addLayout(buttons_layout)
        
        # Totals
        totals_layout = qtw.QHBoxLayout()
        totals_layout.addStretch()
        totals_layout.addWidget(qtw.QLabel("Totals:"))
        
        debit_total = qtw.QLineEdit("$0.00")
        debit_total.setReadOnly(True)
        debit_total.setFixedWidth(100)
        totals_layout.addWidget(debit_total)
        
        credit_total = qtw.QLineEdit("$0.00")
        credit_total.setReadOnly(True)
        credit_total.setFixedWidth(100)
        totals_layout.addWidget(credit_total)
        
        line_items_layout.addLayout(totals_layout)
        
        layout.addWidget(line_items_group)
        
        # Notes
        notes_group = qtw.QGroupBox("Notes")
        notes_layout = qtw.QVBoxLayout(notes_group)
        
        notes_text = qtw.QTextEdit()
        notes_layout.addWidget(notes_text)
        
        layout.addWidget(notes_group)
        
        # Dialog buttons
        buttons = qtw.QDialogButtonBox(qtw.QDialogButtonBox.Save | qtw.QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        # Add a few empty lines to start
        for _ in range(2):
            self.add_journal_line(line_items_table)
        
        if dialog.exec_() == qtw.QDialog.Accepted:
            # In a real app, save to database
            qtw.QMessageBox.information(self, "Success", "Journal entry created successfully!")
            self.load_journal_entries()  # Refresh the table
    
    def add_journal_line(self, table):
        """Add a line to the journal entry table"""
        row = table.rowCount()
        table.insertRow(row)
        
        # Account dropdown
        account_combo = qtw.QComboBox()
        account_combo.addItems([
            "1000 - Cash",
            "1100 - Accounts Receivable",
            "1200 - Inventory",
            "1500 - Office Equipment",
            "2000 - Accounts Payable",
            "4000 - Sales Revenue",
            "5000 - Cost of Goods Sold",
            "6000 - Rent Expense"
        ])
        table.setCellWidget(row, 0, account_combo)
        
        # Description
        description = qtw.QTableWidgetItem("")
        table.setItem(row, 1, description)
        
        # Debit amount
        debit = qtw.QTableWidgetItem("0.00")
        table.setItem(row, 2, debit)
        
        # Credit amount
        credit = qtw.QTableWidgetItem("0.00")
        table.setItem(row, 3, credit)
    
    def remove_journal_line(self, table):
        """Remove a line from the journal entry table"""
        selected_row = table.currentRow()
        if selected_row >= 0:
            table.removeRow(selected_row)
    
    def edit_journal_entry(self, row):
        """Edit a journal entry"""
        # Similar to create_journal_entry but pre-populated
        qtw.QMessageBox.information(self, "Edit Journal Entry", f"Editing entry {self.journal_table.item(row, 1).text()}")

                
        if dialog.exec_() == qtw.QDialog.Accepted:
            # In a real app, save to database
            qtw.QMessageBox.information(self, "Success", "Account created successfully!")
            self.load_chart_of_accounts()  # Refresh the table
    
    def view_journal_details(self, row):
        """View journal entry details"""
        reference = self.journal_table.item(row, 1).text()
        description = self.journal_table.item(row, 2).text()
        
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle(f"Journal Entry: {reference}")
        dialog.setMinimumSize(700, 500)
        
        layout = qtw.QVBoxLayout(dialog)
        
        # Header info
        header_group = qtw.QGroupBox("Entry Information")
        header_layout = qtw.QFormLayout(header_group)
        
        header_layout.addRow("Date:", qtw.QLabel(self.journal_table.item(row, 0).text()))
        header_layout.addRow("Reference:", qtw.QLabel(reference))
        header_layout.addRow("Description:", qtw.QLabel(description))
        header_layout.addRow("Amount:", qtw.QLabel(self.journal_table.item(row, 3).text()))
        
        layout.addWidget(header_group)
        
        # Line items
        line_items_group = qtw.QGroupBox("Journal Entry Lines")
        line_items_layout = qtw.QVBoxLayout(line_items_group)
        
        line_items_table = qtw.QTableWidget(2, 4)
        line_items_table.setHorizontalHeaderLabels(["Account", "Description", "Debit", "Credit"])
        line_items_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        
        # Sample data - would come from database in real app
        if reference == "JE001":
            line_items_table.setItem(0, 0, qtw.QTableWidgetItem("1000 - Cash"))
            line_items_table.setItem(0, 1, qtw.QTableWidgetItem("Initial investment"))
            line_items_table.setItem(0, 2, qtw.QTableWidgetItem("$10,000.00"))
            line_items_table.setItem(0, 3, qtw.QTableWidgetItem("$0.00"))
            
            line_items_table.setItem(1, 0, qtw.QTableWidgetItem("3000 - Owner's Equity"))
            line_items_table.setItem(1, 1, qtw.QTableWidgetItem("Initial investment"))
            line_items_table.setItem(1, 2, qtw.QTableWidgetItem("$0.00"))
            line_items_table.setItem(1, 3, qtw.QTableWidgetItem("$10,000.00"))
        elif reference == "JE002":
            line_items_table.setItem(0, 0, qtw.QTableWidgetItem("1500 - Office Equipment"))
            line_items_table.setItem(0, 1, qtw.QTableWidgetItem("Purchase of equipment"))
            line_items_table.setItem(0, 2, qtw.QTableWidgetItem("$5,000.00"))
            line_items_table.setItem(0, 3, qtw.QTableWidgetItem("$0.00"))
            
            line_items_table.setItem(1, 0, qtw.QTableWidgetItem("1000 - Cash"))
            line_items_table.setItem(1, 1, qtw.QTableWidgetItem("Purchase of equipment"))
            line_items_table.setItem(1, 2, qtw.QTableWidgetItem("$0.00"))
            line_items_table.setItem(1, 3, qtw.QTableWidgetItem("$5,000.00"))
        
        line_items_layout.addWidget(line_items_table)
        
        # Totals
        totals_layout = qtw.QHBoxLayout()
        totals_layout.addStretch()
        totals_layout.addWidget(qtw.QLabel("Totals:"))
        
        amount = self.journal_table.item(row, 3).text().replace("$", "").replace(",", "")
        totals_layout.addWidget(qtw.QLabel(f"${amount}"))
        totals_layout.addWidget(qtw.QLabel(f"${amount}"))
        
        line_items_layout.addLayout(totals_layout)
        
        layout.addWidget(line_items_group)
        
        # Notes
        notes_group = qtw.QGroupBox("Notes")
        notes_layout = qtw.QVBoxLayout(notes_group)
        
        notes_text = qtw.QTextEdit()
        notes_text.setReadOnly(True)
        notes_text.setText("This is a sample journal entry for demonstration purposes.")
        notes_layout.addWidget(notes_text)
        
        layout.addWidget(notes_group)
        
        # Close button
        close_btn = qtw.QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        layout.addWidget(close_btn)
        
        dialog.exec_()
    
    def create_new_customer(self):
        """Create a new customer"""
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle("Create New Customer")
        dialog.setMinimumWidth(500)
        
        layout = qtw.QVBoxLayout(dialog)
        
        tabs = qtw.QTabWidget()
        
        # General info tab
        general_tab = qtw.QWidget()
        general_layout = qtw.QFormLayout(general_tab)
        
        customer_id = qtw.QLineEdit()
        customer_id.setPlaceholderText("Auto-generated if left blank")
        general_layout.addRow("Customer ID:", customer_id)
        
        customer_name = qtw.QLineEdit()
        general_layout.addRow("Customer Name:", customer_name)
        
        contact_name = qtw.QLineEdit()
        general_layout.addRow("Contact Name:", contact_name)
        
        email = qtw.QLineEdit()
        general_layout.addRow("Email:", email)
        
        phone = qtw.QLineEdit()
        general_layout.addRow("Phone:", phone)
        
        website = qtw.QLineEdit()
        general_layout.addRow("Website:", website)
        
        tabs.addTab(general_tab, "General")
        
        # Address tab
        address_tab = qtw.QWidget()
        address_layout = qtw.QFormLayout(address_tab)
        
        billing_address = qtw.QTextEdit()
        address_layout.addRow("Billing Address:", billing_address)
        
        shipping_address = qtw.QTextEdit()
        address_layout.addRow("Shipping Address:", shipping_address)
        
        tabs.addTab(address_tab, "Address")
        
        # Financial tab
        financial_tab = qtw.QWidget()
        financial_layout = qtw.QFormLayout(financial_tab)
        
        credit_limit = qtw.QLineEdit("0.00")
        financial_layout.addRow("Credit Limit:", credit_limit)
        
        payment_terms = qtw.QComboBox()
        payment_terms.addItems(["Net 30", "Net 15", "Due on Receipt", "Net 60"])
        financial_layout.addRow("Payment Terms:", payment_terms)
        
        tax_id = qtw.QLineEdit()
        financial_layout.addRow("Tax ID:", tax_id)
        
        tabs.addTab(financial_tab, "Financial")
        
        # Notes tab
        notes_tab = qtw.QWidget()
        notes_layout = qtw.QVBoxLayout(notes_tab)
        
        notes = qtw.QTextEdit()
        notes_layout.addWidget(notes)
        
        tabs.addTab(notes_tab, "Notes")
        
        layout.addWidget(tabs)
        
        buttons = qtw.QDialogButtonBox(qtw.QDialogButtonBox.Save | qtw.QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        if dialog.exec_() == qtw.QDialog.Accepted:
            # In a real app, save to database
            qtw.QMessageBox.information(self, "Success", "Customer created successfully!")
            self.load_customers()  # Refresh the table
    
    def edit_customer(self, row):
        """Edit a customer"""
        customer_id = self.customers_table.item(row, 0).text()
        customer_name = self.customers_table.item(row, 1).text()
        
        # Similar to create_new_customer but pre-populated
        qtw.QMessageBox.information(self, "Edit Customer", f"Editing customer {customer_name}")
    
    def view_customer_details(self, row):
        """View customer details"""
        customer_id = self.customers_table.item(row, 0).text()
        customer_name = self.customers_table.item(row, 1).text()
        
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle(f"Customer: {customer_name}")
        dialog.setMinimumSize(800, 600)
        
        layout = qtw.QVBoxLayout(dialog)
        
        tabs = qtw.QTabWidget()
        
        # Info tab
        info_tab = qtw.QWidget()
        info_layout = qtw.QFormLayout(info_tab)
        
        info_layout.addRow("Customer ID:", qtw.QLabel(customer_id))
        info_layout.addRow("Customer Name:", qtw.QLabel(customer_name))
        info_layout.addRow("Email:", qtw.QLabel(self.customers_table.item(row, 2).text()))
        info_layout.addRow("Phone:", qtw.QLabel(self.customers_table.item(row, 3).text()))
        info_layout.addRow("Current Balance:", qtw.QLabel(self.customers_table.item(row, 4).text()))
        
        tabs.addTab(info_tab, "Information")
        
        # Invoices tab
        invoices_tab = qtw.QWidget()
        invoices_layout = qtw.QVBoxLayout(invoices_tab)
        
        invoices_table = qtw.QTableWidget(3, 5)
        invoices_table.setHorizontalHeaderLabels(["Invoice #", "Date", "Due Date", "Amount", "Status"])
        invoices_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        
        # Sample data
        sample_invoices = [
            ["INV-001", "2023-05-01", "2023-05-31", "$3,500.00", "Paid"],
            ["INV-002", "2023-05-15", "2023-06-14", "$1,200.00", "Open"],
            ["INV-003", "2023-05-28", "2023-06-27", "$500.00", "Open"]
        ]
        
        for i, invoice in enumerate(sample_invoices):
            for j, value in enumerate(invoice):
                invoices_table.setItem(i, j, qtw.QTableWidgetItem(value))
        
        invoices_layout.addWidget(invoices_table)
        
        tabs.addTab(invoices_tab, "Invoices")
        
        # Transactions tab
        transactions_tab = qtw.QWidget()
        transactions_layout = qtw.QVBoxLayout(transactions_tab)
        
        transactions_table = qtw.QTableWidget(5, 4)
        transactions_table.setHorizontalHeaderLabels(["Date", "Type", "Reference", "Amount"])
        transactions_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        
        # Sample data
        sample_transactions = [
            ["2023-05-01", "Invoice", "INV-001", "$3,500.00"],
            ["2023-05-10", "Payment", "PMT-001", "-$3,500.00"],
            ["2023-05-15", "Invoice", "INV-002", "$1,200.00"],
            ["2023-05-28", "Invoice", "INV-003", "$500.00"],
            ["2023-06-01", "Credit Memo", "CM-001", "-$200.00"]
        ]
        
        for i, transaction in enumerate(sample_transactions):
            for j, value in enumerate(transaction):
                transactions_table.setItem(i, j, qtw.QTableWidgetItem(value))
        
        transactions_layout.addWidget(transactions_table)
        
        tabs.addTab(transactions_tab, "Transactions")
        
        # Notes tab
        notes_tab = qtw.QWidget()
        notes_layout = qtw.QVBoxLayout(notes_tab)
        
        notes = qtw.QTextEdit()
        notes.setReadOnly(True)
        notes.setText("This customer has been with us since 2020. They typically pay on time and order regularly.")
        notes_layout.addWidget(notes)
        
        tabs.addTab(notes_tab, "Notes")
        
        layout.addWidget(tabs)
        
        # Close button
        close_btn = qtw.QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        layout.addWidget(close_btn)
        
        dialog.exec_()
    
    def create_new_vendor(self):
        """Create a new vendor"""
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle("Create New Vendor")
        dialog.setMinimumWidth(500)
        
        layout = qtw.QVBoxLayout(dialog)
        
        tabs = qtw.QTabWidget()
        
        # General info tab
        general_tab = qtw.QWidget()
        general_layout = qtw.QFormLayout(general_tab)
        
        vendor_id = qtw.QLineEdit()
        vendor_id.setPlaceholderText("Auto-generated if left blank")
        general_layout.addRow("Vendor ID:", vendor_id)
        
        vendor_name = qtw.QLineEdit()
        general_layout.addRow("Vendor Name:", vendor_name)
        
        contact_name = qtw.QLineEdit()
        general_layout.addRow("Contact Name:", contact_name)
        
        email = qtw.QLineEdit()
        general_layout.addRow("Email:", email)
        
        phone = qtw.QLineEdit()
        general_layout.addRow("Phone:", phone)
        
        website = qtw.QLineEdit()
        general_layout.addRow("Website:", website)
        
        tabs.addTab(general_tab, "General")
        
        # Address tab
        address_tab = qtw.QWidget()
        address_layout = qtw.QFormLayout(address_tab)
        
        billing_address = qtw.QTextEdit()
        address_layout.addRow("Billing Address:", billing_address)
        
        shipping_address = qtw.QTextEdit()
        address_layout.addRow("Shipping Address:", shipping_address)
        
        tabs.addTab(address_tab, "Address")
        
        # Financial tab
        financial_tab = qtw.QWidget()
        financial_layout = qtw.QFormLayout(financial_tab)
        
        payment_terms = qtw.QComboBox()
        payment_terms.addItems(["Net 30", "Net 15", "Due on Receipt", "Net 60"])
        financial_layout.addRow("Payment Terms:", payment_terms)
        
        tax_id = qtw.QLineEdit()
        financial_layout.addRow("Tax ID:", tax_id)
        
        tabs.addTab(financial_tab, "Financial")
        
        # Notes tab
        notes_tab = qtw.QWidget()
        notes_layout = qtw.QVBoxLayout(notes_tab)
        
        notes = qtw.QTextEdit()
        notes_layout.addWidget(notes)
        
        tabs.addTab(notes_tab, "Notes")
        
        layout.addWidget(tabs)
        
        buttons = qtw.QDialogButtonBox(qtw.QDialogButtonBox.Save | qtw.QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        if dialog.exec_() == qtw.QDialog.Accepted:
            # In a real app, save to database
            qtw.QMessageBox.information(self, "Success", "Vendor created successfully!")
            self.load_vendors()  # Refresh the table
    
    def edit_vendor(self, row):
        """Edit a vendor"""
        vendor_id = self.vendors_table.item(row, 0).text()
        vendor_name = self.vendors_table.item(row, 1).text()
        
        # Similar to create_new_vendor but pre-populated
        qtw.QMessageBox.information(self, "Edit Vendor", f"Editing vendor {vendor_name}")
    
    def view_vendor_details(self, row):
        """View vendor details"""
        vendor_id = self.vendors_table.item(row, 0).text()
        vendor_name = self.vendors_table.item(row, 1).text()
        
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle(f"Vendor: {vendor_name}")
        dialog.setMinimumSize(800, 600)
        
        layout = qtw.QVBoxLayout(dialog)
        
        tabs = qtw.QTabWidget()
        
        # Info tab
        info_tab = qtw.QWidget()
        info_layout = qtw.QFormLayout(info_tab)
        
        info_layout.addRow("Vendor ID:", qtw.QLabel(vendor_id))
        info_layout.addRow("Vendor Name:", qtw.QLabel(vendor_name))
        info_layout.addRow("Email:", qtw.QLabel(self.vendors_table.item(row, 2).text()))
        info_layout.addRow("Phone:", qtw.QLabel(self.vendors_table.item(row, 3).text()))
        info_layout.addRow("Current Balance:", qtw.QLabel(self.vendors_table.item(row, 4).text()))
        
        tabs.addTab(info_tab, "Information")
        
        # Bills tab
        bills_tab = qtw.QWidget()
        bills_layout = qtw.QVBoxLayout(bills_tab)
        
        bills_table = qtw.QTableWidget(3, 5)
        bills_table.setHorizontalHeaderLabels(["Bill #", "Date", "Due Date", "Amount", "Status"])
        bills_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        
        # Sample data
        sample_bills = [
            ["BILL-001", "2023-05-01", "2023-05-31", "$2,500.00", "Paid"],
            ["BILL-002", "2023-05-15", "2023-06-14", "$1,800.00", "Open"],
            ["BILL-003", "2023-05-28", "2023-06-27", "$750.00", "Open"]
        ]
        
        for i, bill in enumerate(sample_bills):
            for j, value in enumerate(bill):
                bills_table.setItem(i, j, qtw.QTableWidgetItem(value))
        
        bills_layout.addWidget(bills_table)
        
        tabs.addTab(bills_tab, "Bills")
        
        # Transactions tab
        transactions_tab = qtw.QWidget()
        transactions_layout = qtw.QVBoxLayout(transactions_tab)
        
        transactions_table = qtw.QTableWidget(5, 4)
        transactions_table.setHorizontalHeaderLabels(["Date", "Type", "Reference", "Amount"])
        transactions_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        
        # Sample data
        sample_transactions = [
            ["2023-05-01", "Bill", "BILL-001", "$2,500.00"],
            ["2023-05-10", "Payment", "PMT-001", "-$2,500.00"],
            ["2023-05-15", "Bill", "BILL-002", "$1,800.00"],
            ["2023-05-28", "Bill", "BILL-003", "$750.00"],
            ["2023-06-01", "Credit", "CR-001", "-$100.00"]
        ]
        
        for i, transaction in enumerate(sample_transactions):
            for j, value in enumerate(transaction):
                transactions_table.setItem(i, j, qtw.QTableWidgetItem(value))
        
        transactions_layout.addWidget(transactions_table)
        
        tabs.addTab(transactions_tab, "Transactions")
        
        # Notes tab
        notes_tab = qtw.QWidget()
        notes_layout = qtw.QVBoxLayout(notes_tab)
        
        notes = qtw.QTextEdit()
        notes.setReadOnly(True)
        notes.setText("This vendor provides quality products with occasional delays in shipping.")
        notes_layout.addWidget(notes)
        
        tabs.addTab(notes_tab, "Notes")
        
        layout.addWidget(tabs)
        
        # Close button
        close_btn = qtw.QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        layout.addWidget(close_btn)
        
        dialog.exec_()
    
    def create_invoice(self):
        """Create a new invoice"""
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle("Create New Invoice")
        dialog.setMinimumSize(800, 600)

        layout = qtw.QVBoxLayout(dialog)

        # Header info
        header_group = qtw.QGroupBox("Invoice Information")
        header_layout = qtw.QGridLayout(header_group)

        # Left column
        header_layout.addWidget(qtw.QLabel("Invoice #:"), 0, 0)
        invoice_number = qtw.QLineEdit("INV-" + str(random.randint(1000, 9999)))
        header_layout.addWidget(invoice_number, 0, 1)

        header_layout.addWidget(qtw.QLabel("Date:"), 1, 0)
        invoice_date = qtw.QDateEdit(qtw.QDate.currentDate())
        header_layout.addWidget(invoice_date, 1, 1)

        header_layout.addWidget(qtw.QLabel("Due Date:"), 2, 0)
        due_date = qtw.QDateEdit(qtw.QDate.currentDate().addDays(30))
        header_layout.addWidget(due_date, 2, 1)

        # Right column
        header_layout.addWidget(qtw.QLabel("Customer:"), 0, 2)
        customer_combo = qtw.QComboBox()
        customer_combo.addItems(["ABC Company", "XYZ Corporation", "Acme Inc."])
        header_layout.addWidget(customer_combo, 0, 3)

        header_layout.addWidget(qtw.QLabel("Payment Terms:"), 1, 2)
        terms_combo = qtw.QComboBox()
        terms_combo.addItems(["Net 30", "Net 15", "Due on Receipt"])
        header_layout.addWidget(terms_combo, 1, 3)

        header_layout.addWidget(qtw.QLabel("Reference:"), 2, 2)
        reference = qtw.QLineEdit()
        reference.setPlaceholderText("PO number or reference")
        header_layout.addWidget(reference, 2, 3)

        layout.addWidget(header_group)

        # Line items
        items_group = qtw.QGroupBox("Invoice Items")
        items_layout = qtw.QVBoxLayout(items_group)

        items_table = qtw.QTableWidget(0, 5)
        items_table.setHorizontalHeaderLabels(["Item", "Description", "Quantity", "Price", "Amount"])
        items_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)

        items_layout.addWidget(items_table)

        # Add/remove buttons
        buttons_layout = qtw.QHBoxLayout()

        add_item_btn = qtw.QPushButton("Add Item")
        add_item_btn.clicked.connect(lambda: self.add_invoice_item(items_table))
        buttons_layout.addWidget(add_item_btn)

        remove_item_btn = qtw.QPushButton("Remove Item")
        remove_item_btn.clicked.connect(lambda: self.remove_invoice_item(items_table))
        buttons_layout.addWidget(remove_item_btn)

        items_layout.addLayout(buttons_layout)

        # Totals
        totals_layout = qtw.QFormLayout()
        totals_layout.setFieldGrowthPolicy(qtw.QFormLayout.AllNonFixedFieldsGrow)

        subtotal = qtw.QLineEdit("$0.00")
        subtotal.setReadOnly(True)
        subtotal.setAlignment(qtc.Qt.AlignRight)
        totals_layout.addRow("Subtotal:", subtotal)

        tax = qtw.QLineEdit("$0.00")
        tax.setReadOnly(True)
        tax.setAlignment(qtc.Qt.AlignRight)
        totals_layout.addRow("Tax:", tax)

        total = qtw.QLineEdit("$0.00")
        total.setReadOnly(True)
        total.setAlignment(qtc.Qt.AlignRight)
        totals_layout.addRow("Total:", total)

        items_layout.addLayout(totals_layout)

        layout.addWidget(items_group)

        # Notes
        notes_group = qtw.QGroupBox("Notes")
        notes_layout = qtw.QVBoxLayout(notes_group)

        notes_text = qtw.QTextEdit()
        notes_text.setPlaceholderText("Enter any notes or payment instructions here...")
        notes_layout.addWidget(notes_text)

        layout.addWidget(notes_group)

        # Dialog buttons
        buttons = qtw.QDialogButtonBox(qtw.QDialogButtonBox.Save | qtw.QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)

        # Add a few empty lines to start
        for _ in range(3):
            self.add_invoice_item(items_table)

        if dialog.exec_() == qtw.QDialog.Accepted:
            # In a real app, save to database
            qtw.QMessageBox.information(self, "Success", "Invoice created successfully!")
            self.load_invoices()  # Refresh the table
    
    def add_invoice_item(self, table):
        """Add an item to the invoice table"""
        row = table.rowCount()
        table.insertRow(row)
        
        # Item dropdown
        item_combo = qtw.QComboBox()
        item_combo.addItems([
            "Product A",
            "Product B",
            "Service 1",
            "Service 2",
            "Consultation"
        ])
        table.setCellWidget(row, 0, item_combo)
        
        # Description
        description = qtw.QTableWidgetItem("Description")
        table.setItem(row, 1, description)
        
        # Quantity
        quantity = qtw.QTableWidgetItem("1")
        table.setItem(row, 2, quantity)
        
        # Price
        price = qtw.QTableWidgetItem("0.00")
        table.setItem(row, 3, price)
        
        # Amount (calculated)
        amount = qtw.QTableWidgetItem("0.00")
        table.setItem(row, 4, amount)
    
    def remove_invoice_item(self, table):
        """Remove an item from the invoice table"""
        selected_row = table.currentRow()
        if selected_row >= 0:
            table.removeRow(selected_row)
    
    def create_bill(self):
        """Create a new bill"""
        dialog = qtw.QDialog(self)
        dialog.setWindowTitle("Create New Bill")
        dialog.setMinimumSize(800, 600)
        
        layout = qtw.QVBoxLayout(dialog)
        
        # Header info
        header_group = qtw.QGroupBox("Bill Information")
        header_layout = qtw.QGridLayout(header_group)
        
        # Left column
        header_layout.addWidget(qtw.QLabel("Bill #:"), 0, 0)
        bill_number = qtw.QLineEdit("BILL-" + str(random.randint(1000, 9999)))
        header_layout.addWidget(bill_number, 0, 1)
        
        header_layout.addWidget(qtw.QLabel("Date:"), 1, 0)
        bill_date = qtw.QDateEdit(qtc.QDate.currentDate())
        header_layout.addWidget(bill_date, 1, 1)
        
        header_layout.addWidget(qtw.QLabel("Due Date:"), 2, 0)
        due_date = qtw.QDateEdit(qtc.QDate.currentDate().addDays(30))
        header_layout.addWidget(due_date, 2, 1)
        
        # Right column
        header_layout.addWidget(qtw.QLabel("Vendor:"), 0, 2)
        vendor_combo = qtw.QComboBox()
        vendor_combo.addItems(["Supplier A", "Supplier B", "Contractor C"])
        header_layout.addWidget(vendor_combo, 0, 3)
        
        header_layout.addWidget(qtw.QLabel("Payment Terms:"), 1, 2)
        terms_combo = qtw.QComboBox()
        terms_combo.addItems(["Net 30", "Net 15", "Due on Receipt"])
        header_layout.addWidget(terms_combo, 1, 3)
        
        header_layout.addWidget(qtw.QLabel("Reference:"), 2, 2)
        reference = qtw.QLineEdit()
        reference.setPlaceholderText("Vendor invoice number")
        header_layout.addWidget(reference, 2, 3)
        
        layout.addWidget(header_group)
        
        # Line items
        items_group = qtw.QGroupBox("Bill Items")
        items_layout = qtw.QVBoxLayout(items_group)
        
        items_table = qtw.QTableWidget(0, 5)
        items_table.setHorizontalHeaderLabels(["Account", "Description", "Quantity", "Price", "Amount"])
        items_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)

        items_layout.addWidget(items_table)
        
        # Add/remove buttons
        buttons_layout = qtw.QHBoxLayout()
        
        add_item_btn = qtw.QPushButton("Add Item")
        add_item_btn.clicked.connect(lambda: self.add_bill_item(items_table))
        buttons_layout.addWidget(add_item_btn)
        
        remove_item_btn = qtw.QPushButton("Remove Item")
        remove_item_btn.clicked.connect(lambda: self.remove_bill_item(items_table))
        buttons_layout.addWidget(remove_item_btn)
        
        items_layout.addLayout(buttons_layout)
        
        # Totals
        totals_layout = qtw.QFormLayout()
        totals_layout.setFieldGrowthPolicy(qtw.QFormLayout.AllNonFixedFieldsGrow)
        
        subtotal = qtw.QLineEdit("$0.00")
        subtotal.setReadOnly(True)
        subtotal.setAlignment(qtc.Qt.AlignRight)
        totals_layout.addRow("Subtotal:", subtotal)
        
        tax = qtw.QLineEdit("$0.00")
        tax.setReadOnly(True)
        tax.setAlignment(qtc.Qt.AlignRight)
        totals_layout.addRow("Tax:", tax)
        
        total = qtw.QLineEdit("$0.00")
        total.setReadOnly(True)
        total.setAlignment(qtc.Qt.AlignRight)
        totals_layout.addRow("Total:", total)
        
        items_layout.addLayout(totals_layout)
        
        layout.addWidget(items_group)
        
        # Notes
        notes_group = qtw.QGroupBox("Notes")
        notes_layout = qtw.QVBoxLayout(notes_group)
        
        notes_text = qtw.QTextEdit()
        notes_text.setPlaceholderText("Enter any notes about this bill...")
        notes_layout.addWidget(notes_text)
        
        layout.addWidget(notes_group)
        
        # Dialog buttons
        buttons = qtw.QDialogButtonBox(qtw.QDialogButtonBox.Save | qtw.QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        # Add a few empty lines to start
        for _ in range(3):
            self.add_bill_item(items_table)
        
        if dialog.exec_() == qtw.QDialog.Accepted:
            # In a real app, save to database
            qtw.QMessageBox.information(self, "Success", "Bill created successfully!")
            self.load_bills()  # Refresh the table
    
    def add_bill_item(self, table):
        """Add an item to the bill table"""
        row = table.rowCount()
        table.insertRow(row)
        
        # Account dropdown
        account_combo = qtw.QComboBox()
        account_combo.addItems([
            "5000 - Cost of Goods Sold",
            "6000 - Rent Expense",
            "6100 - Office Supplies",
            "6200 - Utilities",
            "1200 - Inventory"
        ])
        table.setCellWidget(row, 0, account_combo)
        
        # Description
        description = qtw.QTableWidgetItem("Description")
        table.setItem(row, 1, description)
        
        # Quantity
        quantity = qtw.QTableWidgetItem("1")
        table.setItem(row, 2, quantity)
        
        # Price
        price = qtw.QTableWidgetItem("0.00")
        table.setItem(row, 3, price)
        
        # Amount (calculated)
        amount = qtw.QTableWidgetItem("0.00")
        table.setItem(row, 4, amount)
    
    def remove_bill_item(self, table):
        """Remove an item from the bill table"""
        selected_row = table.currentRow()
        if selected_row >= 0:
            table.removeRow(selected_row)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    
    # Set application style
    app.setStyle("Fusion")
    
    # Apply dark theme
    palette = qtw.QPalette()
    palette.setColor(qtg.QPalette.Window, qtg.QColor(53, 53, 53))
    palette.setColor(qtg.QPalette.WindowText, qtc.Qt.white)
    palette.setColor(qtg.QPalette.Base, qtg.QColor(25, 25, 25))
    palette.setColor(qtg.QPalette.AlternateBase, qtg.QColor(53, 53, 53))
    palette.setColor(qtg.QPalette.ToolTipBase, qtc.Qt.white)
    palette.setColor(qtg.QPalette.ToolTipText, qtc.Qt.white)
    palette.setColor(qtg.QPalette.Text, qtc.Qt.white)
    palette.setColor(qtg.QPalette.Button, qtg.QColor(53, 53, 53))
    palette.setColor(qtg.QPalette.ButtonText, qtc.Qt.white)
    palette.setColor(qtg.QPalette.BrightText, qtc.Qt.red)
    palette.setColor(qtg.QPalette.Link, qtg.QColor(42, 130, 218))
    palette.setColor(qtg.QPalette.Highlight, qtg.QColor(42, 130, 218))
    palette.setColor(qtg.QPalette.HighlightedText, qtc.Qt.black)
    app.setPalette(palette)
    
    window = AccountingApp()
    window.show()
    
    sys.exit(app.exec_())