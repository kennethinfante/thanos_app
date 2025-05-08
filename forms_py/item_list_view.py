from PyQt5 import QtCore, QtGui, QtWidgets
from .styles_macos import *

class Ui_itemListView(object):
    def setupUi(self, itemsView):
        # Main window setup
        itemsView.setObjectName("itemsView")
        # Appropriate size for MacBook Pro 2015 with Retina display
        itemsView.resize(1440, 900)
        itemsView.setMinimumSize(QtCore.QSize(1024, 768))
        itemsView.setMaximumSize(QtCore.QSize(1920, 1080))

        # Central widget
        self.centralwidget = QtWidgets.QWidget(itemsView)
        self.centralwidget.setObjectName("centralwidget")

        # Main vertical layout for the entire form
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        # Search criteria layout (horizontal)
        self.search_hbox = QtWidgets.QHBoxLayout()
        self.search_hbox.setSpacing(10)
        self.search_hbox.setObjectName("search_hbox")

        # Item name label
        self.item_name_label = QtWidgets.QLabel(self.centralwidget)
        self.item_name_label.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)  # Slightly larger for Retina display
        font.setBold(True)
        self.item_name_label.setFont(font)
        self.item_name_label.setText("Item Name")
        self.item_name_label.setObjectName("item_name_label")
        self.search_hbox.addWidget(self.item_name_label)

        # Item name line edit
        self.item_name_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.item_name_line_edit.setMinimumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(13)  # Slightly larger for Retina display
        self.item_name_line_edit.setFont(font)
        self.item_name_line_edit.setObjectName("item_name_line_edit")
        self.search_hbox.addWidget(self.item_name_line_edit)

        # Add flexible space to push buttons to the right
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.search_hbox.addItem(spacer_item)

        # Search button
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)  # Slightly larger for Retina display
        font.setBold(True)
        self.search_btn.setFont(font)
        self.search_btn.setText("Search")
        self.search_btn.setObjectName("search_btn")
        self.search_hbox.addWidget(self.search_btn)

        # Clear button
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)  # Slightly larger for Retina display
        font.setBold(True)
        self.clear_btn.setFont(font)
        self.clear_btn.setText("Clear")
        self.clear_btn.setObjectName("clear_btn")
        self.search_hbox.addWidget(self.clear_btn)

        # Add new item button
        self.add_new_item_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_item_btn.setMinimumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setPointSize(13)  # Slightly larger for Retina display
        font.setBold(True)
        self.add_new_item_btn.setFont(font)
        self.add_new_item_btn.setText("Add New Item")
        self.add_new_item_btn.setObjectName("add_new_item_btn")
        self.search_hbox.addWidget(self.add_new_item_btn)

        # Add search criteria layout to main layout
        self.verticalLayout.addLayout(self.search_hbox)

        # Table view for items
        self.items_table_view = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.items_table_view.setSizePolicy(sizePolicy)
        self.items_table_view.setObjectName("items_table_view")

        # Configure table headers
        self.items_table_view.horizontalHeader().setDefaultSectionSize(150)  # Slightly larger for Retina display
        self.items_table_view.horizontalHeader().setMinimumSectionSize(100)  # Slightly larger for Retina display
        self.items_table_view.horizontalHeader().setStretchLastSection(True)

        # Set selection behavior to select entire rows
        self.items_table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Set alternating row colors for better readability
        self.items_table_view.setAlternatingRowColors(True)

        # Add table view to main layout
        self.verticalLayout.addWidget(self.items_table_view)

        # Set central widget
        itemsView.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(itemsView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))  # macOS menu height is typically 22px
        self.menubar.setObjectName("menubar")
        itemsView.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(itemsView)
        self.statusbar.setObjectName("statusbar")
        itemsView.setStatusBar(self.statusbar)

        # Set window title
        itemsView.setWindowTitle("Items")

        # Connect signals and slots
        QtCore.QMetaObject.connectSlotsByName(itemsView)

        # Apply macOS-specific style adjustments
        apply_button_style(self.search_btn)
        apply_button_style(self.clear_btn)
        apply_button_style(self.add_new_item_btn)

        apply_table_style(self.items_table_view)
        apply_line_edit_style(self.item_name_line_edit)
