from PyQt5 import QtCore, QtGui, QtWidgets
from .form_styles import *
from .form_utils import *

class Ui_itemListView(object):
    def setupUi(self, itemListView):
        # Main window setup
        itemListView.setObjectName("itemListView")
        # Appropriate size for MacBook Pro 2015 with Retina display
        itemListView.resize(1440, 900)
        itemListView.setMinimumSize(QtCore.QSize(1440, 900))
        itemListView.setMaximumSize(QtCore.QSize(1920, 1080))

        # Central widget
        self.central_widget = QtWidgets.QWidget(itemListView)
        self.central_widget.setObjectName("central_widget")

        # Main vertical layout for the entire form
        self.main_vly = QtWidgets.QVBoxLayout(self.central_widget)
        self.main_vly.setContentsMargins(10, 10, 10, 10)
        self.main_vly.setSpacing(10)
        self.main_vly.setObjectName("main_vly")

        # Search section
        self.header_section = QtWidgets.QWidget(self.central_widget)
        self.header_section.setObjectName("header_section")

        self.header_hly = QtWidgets.QHBoxLayout(self.header_section)
        # self.header_vly.setContentsMargins(0, 0, 0, 0)
        self.header_hly.setSpacing(10)
        self.header_hly.setObjectName("header_vly")

        # Item Name label
        self.item_name_lbl = create_label(self.header_section, "Item Name")
        self.header_hly.addWidget(self.item_name_lbl)

        # Item line edit
        self.item_name_lne = create_line_edit(self.header_section)
        self.header_hly.addWidget(self.item_name_lne)

        # Search button
        self.search_btn = create_button(self.header_section, "Search")
        self.header_hly.addWidget(self.search_btn)

        # Clear button
        self.clear_btn = create_button(self.header_section, "Clear")
        self.header_hly.addWidget(self.clear_btn)

        # Clear button
        self.add_new_item_btn = create_button(self.header_section, "Add New Item")
        self.header_hly.addWidget(self.add_new_item_btn)

        # Add header section to main layout
        self.main_vly.addWidget(self.header_section)

        # Table view for invoices
        self.items_table_view = QtWidgets.QTableView(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.items_table_view.setSizePolicy(sizePolicy)
        self.items_table_view.setObjectName("items_table_view")

        # Configure table headers
        self.items_table_view.horizontalHeader().setDefaultSectionSize(120)
        self.items_table_view.horizontalHeader().setMinimumSectionSize(80)

        # Make all columns stretch proportionally when the window is resized
        self.items_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Set resize mode for each column individually
        # First, set all columns to stretch
        # header = self.items_table_view.horizontalHeader()
        # for i in range(header.count()):
        #     header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        # Then, set specific columns to fixed width if needed
        # For example, if column 0 is an ID column that should stay fixed width:
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        # self.items_table_view.setColumnWidth(0, 60)  # Set fixed width for column 0

        # Add table view to main layout
        self.main_vly.addWidget(self.items_table_view)

        # Set central widget
        itemListView.setCentralWidget(self.central_widget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(itemListView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))  # macOS menu height is typically 22px
        self.menubar.setObjectName("menubar")
        itemListView.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(itemListView)
        self.statusbar.setObjectName("statusbar")
        itemListView.setStatusBar(self.statusbar)

        # Set window title
        itemListView.setWindowTitle("Invoices")

        # Connect signals and slots
        QtCore.QMetaObject.connectSlotsByName(itemListView)

        # Apply macOS-specific style adjustments
        apply_button_style(self.search_btn)
        apply_button_style(self.clear_btn)
        apply_button_style(self.add_new_item_btn)

        apply_table_style(self.items_table_view)

        apply_line_edit_style(self.item_name_lne)


