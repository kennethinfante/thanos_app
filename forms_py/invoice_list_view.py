from PyQt5 import QtCore, QtGui, QtWidgets
from .form_styles import *

class Ui_invoiceListView(object):
    def setupUi(self, invoiceListView):
        # Main window setup
        invoiceListView.setObjectName("invoiceListView")
        # Appropriate size for MacBook Pro 2015 with Retina display
        invoiceListView.resize(1440, 900)
        invoiceListView.setMinimumSize(QtCore.QSize(1024, 768))
        invoiceListView.setMaximumSize(QtCore.QSize(1920, 1080))

        # Central widget
        self.centralwidget = QtWidgets.QWidget(invoiceListView)
        self.centralwidget.setObjectName("centralwidget")

        # Main vertical layout for the entire form
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName("main_layout")

        # Search section
        self.search_section = QtWidgets.QWidget(self.centralwidget)
        self.search_section.setObjectName("search_section")
        self.search_layout = QtWidgets.QVBoxLayout(self.search_section)
        self.search_layout.setContentsMargins(0, 0, 0, 0)
        self.search_layout.setSpacing(10)
        self.search_layout.setObjectName("search_layout")

        # Search criteria layout (horizontal)
        self.search_hbox = QtWidgets.QHBoxLayout()
        self.search_hbox.setSpacing(10)
        self.search_hbox.setObjectName("search_hbox")

        # Date filter checkbox
        self.search_date_chbox = QtWidgets.QCheckBox(self.search_section)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.search_date_chbox.setFont(font)
        self.search_date_chbox.setText("Enable date")
        self.search_date_chbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.search_date_chbox.setObjectName("search_date_chbox")
        self.search_hbox.addWidget(self.search_date_chbox)

        # From date label
        self.from_date_label = QtWidgets.QLabel(self.search_section)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.from_date_label.setFont(font)
        self.from_date_label.setText("From date:")
        self.from_date_label.setObjectName("from_date_label")
        self.search_hbox.addWidget(self.from_date_label)

        # From date edit
        self.from_date_edit = QtWidgets.QDateEdit(self.search_section)
        self.from_date_edit.setEnabled(False)
        self.from_date_edit.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.from_date_edit.setFont(font)
        self.from_date_edit.setCalendarPopup(True)
        self.from_date_edit.setDate(QtCore.QDate(2022, 1, 1))
        self.from_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.from_date_edit.setObjectName("from_date_edit")
        self.search_hbox.addWidget(self.from_date_edit)

        # To date label
        self.to_date_label = QtWidgets.QLabel(self.search_section)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.to_date_label.setFont(font)
        self.to_date_label.setText("To:")
        self.to_date_label.setObjectName("to_date_label")
        self.search_hbox.addWidget(self.to_date_label)

        # To date edit
        self.to_date_edit = QtWidgets.QDateEdit(self.search_section)
        self.to_date_edit.setEnabled(False)
        self.to_date_edit.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.to_date_edit.setFont(font)
        self.to_date_edit.setCalendarPopup(True)
        self.to_date_edit.setDate(QtCore.QDate(2024, 1, 1))
        self.to_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.to_date_edit.setObjectName("to_date_edit")
        self.search_hbox.addWidget(self.to_date_edit)

        # Customer label
        self.customer_label = QtWidgets.QLabel(self.search_section)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.customer_label.setFont(font)
        self.customer_label.setText("Customer")
        self.customer_label.setObjectName("customer_label")
        self.search_hbox.addWidget(self.customer_label)

        # Customer line edit
        self.customer_line_edit = QtWidgets.QLineEdit(self.search_section)
        self.customer_line_edit.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customer_line_edit.setFont(font)
        self.customer_line_edit.setObjectName("customer_line_edit")
        self.search_hbox.addWidget(self.customer_line_edit)

        # Search button
        self.search_btn = QtWidgets.QPushButton(self.search_section)
        self.search_btn.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.search_btn.setFont(font)
        self.search_btn.setText("Search")
        self.search_btn.setObjectName("search_btn")
        self.search_hbox.addWidget(self.search_btn)

        # Clear button
        self.clear_btn = QtWidgets.QPushButton(self.search_section)
        self.clear_btn.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.clear_btn.setFont(font)
        self.clear_btn.setText("Clear")
        self.clear_btn.setObjectName("clear_btn")
        self.search_hbox.addWidget(self.clear_btn)

        # Add search criteria layout to search section
        self.search_layout.addLayout(self.search_hbox)

        # Action buttons layout (horizontal)
        self.btn_hbox = QtWidgets.QHBoxLayout()
        self.btn_hbox.setSpacing(10)
        self.btn_hbox.setObjectName("btn_hbox")

        # Add new invoice button
        self.add_new_invoice_btn = QtWidgets.QPushButton(self.search_section)
        self.add_new_invoice_btn.setMinimumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.add_new_invoice_btn.setFont(font)
        self.add_new_invoice_btn.setText("Add New Invoice")
        self.add_new_invoice_btn.setObjectName("add_new_invoice_btn")
        self.btn_hbox.addWidget(self.add_new_invoice_btn)

        # Refresh list button
        self.refresh_list_btn = QtWidgets.QPushButton(self.search_section)
        self.refresh_list_btn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.refresh_list_btn.setFont(font)
        self.refresh_list_btn.setText("Refresh List")
        self.refresh_list_btn.setObjectName("refresh_list_btn")
        self.btn_hbox.addWidget(self.refresh_list_btn)

        # Add spacer to push buttons to the left
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn_hbox.addItem(spacer_item)

        # Add action buttons layout to search section
        self.search_layout.addLayout(self.btn_hbox)

        # Add search section to main layout
        self.main_layout.addWidget(self.search_section)

        # Table view for invoices
        self.invoices_table_view = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.invoices_table_view.setSizePolicy(sizePolicy)
        self.invoices_table_view.setObjectName("invoices_table_view")

        # Configure table headers
        self.invoices_table_view.horizontalHeader().setDefaultSectionSize(120)
        self.invoices_table_view.horizontalHeader().setMinimumSectionSize(80)
        self.invoices_table_view.horizontalHeader().setStretchLastSection(True)

        # Add table view to main layout
        self.main_layout.addWidget(self.invoices_table_view)

        # Set central widget
        invoiceListView.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(invoiceListView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))  # macOS menu height is typically 22px
        self.menubar.setObjectName("menubar")
        invoiceListView.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(invoiceListView)
        self.statusbar.setObjectName("statusbar")
        invoiceListView.setStatusBar(self.statusbar)

        # Set window title
        invoiceListView.setWindowTitle("Invoices")

        # Connect signals and slots
        QtCore.QMetaObject.connectSlotsByName(invoiceListView)

        # Apply macOS-specific style adjustments
        apply_button_style(self.search_btn)
        apply_button_style(self.clear_btn)
        apply_button_style(self.add_new_invoice_btn)
        apply_button_style(self.refresh_list_btn)

        apply_table_style(self.invoices_table_view)

        apply_line_edit_style(self.customer_line_edit)
