from PyQt5 import QtCore, QtGui, QtWidgets
from .form_styles import *
from .form_utils import *

class Ui_invoiceListView(object):
    def setupUi(self, invoiceListView):
        # Main window setup
        invoiceListView.setObjectName("invoiceListView")
        # Appropriate size for MacBook Pro 2015 with Retina display
        invoiceListView.resize(*page_min_size)
        invoiceListView.setMinimumSize(QtCore.QSize(*page_min_size))
        invoiceListView.setMaximumSize(QtCore.QSize(*page_max_size))

        # Set size policy to prefer the minimum size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(invoiceListView.sizePolicy().hasHeightForWidth())
        invoiceListView.setSizePolicy(sizePolicy)
        
        # Central widget
        self.central_widget = QtWidgets.QWidget(invoiceListView)
        self.central_widget.setObjectName("central_widget")

        # Main vertical layout for the entire form
        self.main_vly = QtWidgets.QVBoxLayout(self.central_widget)
        self.main_vly.setContentsMargins(10, 10, 10, 10)
        self.main_vly.setSpacing(10)
        self.main_vly.setObjectName("main_vly")

        # Header section
        self.header_section = QtWidgets.QWidget(self.central_widget)
        self.header_section.setObjectName("header_section")
        self.header_vly = QtWidgets.QVBoxLayout(self.header_section)
        # self.header_vly.setContentsMargins(0, 0, 0, 0)
        self.header_vly.setSpacing(10)
        self.header_vly.setObjectName("header_vly")

        # Search criteria layout (horizontal)
        self.search_hly = QtWidgets.QHBoxLayout()
        self.search_hly.setSpacing(10)
        self.search_hly.setObjectName("search_hly")

        # Date filter checkbox
        self.search_date_chbox = create_checkbox(self.header_section, "Enable date")
        self.search_hly.addWidget(self.search_date_chbox)

        # From date label
        self.from_date_lbl = create_label(self.header_section, "From date:")
        self.search_hly.addWidget(self.from_date_lbl)

        # From date edit
        self.from_date_dte = create_date_edit(self.header_section, False, default_date=(2022, 1, 1))
        self.search_hly.addWidget(self.from_date_dte)

        # To date label
        self.to_date_lbl = create_label(self.header_section, "To date:")
        self.search_hly.addWidget(self.to_date_lbl)

        # To date edit
        self.to_date_dte = create_date_edit(self.header_section, False, default_date=(2024, 1, 1))
        self.search_hly.addWidget(self.to_date_dte)

        # Customer label
        self.customer_lbl = create_label(self.header_section, "Customer")
        self.search_hly.addWidget(self.customer_lbl)

        # Customer line edit
        self.customer_lne = create_line_edit(self.header_section, placeholder="Enter customer name")
        self.search_hly.addWidget(self.customer_lne)

        # Search button
        self.search_btn = create_button(self.header_section, "Search")
        self.search_hly.addWidget(self.search_btn)

        # Clear button
        self.clear_btn = create_button(self.header_section, "Clear")
        self.search_hly.addWidget(self.clear_btn)

        # Add search criteria layout to search section
        self.header_vly.addLayout(self.search_hly)

        # Action buttons layout (horizontal)
        self.btn_hly = QtWidgets.QHBoxLayout()
        self.btn_hly.setSpacing(10)
        self.btn_hly.setObjectName("btn_hly")

        # Add new invoice button
        self.add_new_invoice_btn = create_button(self.header_section, "Add New Invoice", min_size=(180, 40))
        self.btn_hly.addWidget(self.add_new_invoice_btn)

        # Refresh list button
        self.refresh_list_btn = create_button(self.header_section, "Refresh List", min_size=(150, 40))
        self.btn_hly.addWidget(self.refresh_list_btn)

        # Add spacer to push buttons to the left
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn_hly.addItem(spacer_item)

        # Add action buttons layout to search section
        self.header_vly.addLayout(self.btn_hly)

        # Add header section to main layout
        self.main_vly.addWidget(self.header_section)

        # Table view for invoices
        self.invoices_table_view = QtWidgets.QTableView(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.invoices_table_view.setSizePolicy(sizePolicy)
        self.invoices_table_view.setObjectName("invoices_table_view")

        # Configure table headers
        self.invoices_table_view.horizontalHeader().setDefaultSectionSize(120)
        self.invoices_table_view.horizontalHeader().setMinimumSectionSize(80)

        # Add table view to main layout
        self.main_vly.addWidget(self.invoices_table_view)

        # Set central widget
        invoiceListView.setCentralWidget(self.central_widget)

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

        apply_line_edit_style(self.customer_lne)
