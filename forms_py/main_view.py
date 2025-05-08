import resources_rc
from .styles_macos import *

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainView(object):
    def setupUi(self, MainView):
        # Main window setup
        MainView.setObjectName("MainView")
        # Appropriate size for MacBook Pro 2015 with Retina display
        MainView.resize(1440, 900)
        MainView.setMinimumSize(QtCore.QSize(1024, 768))
        MainView.setMaximumSize(QtCore.QSize(1920, 1080))

        # Base stylesheet - more macOS-like
        apply_main_window_style(MainView)

        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainView)
        self.centralwidget.setObjectName("centralwidget")

        # Main horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)  # Remove margins for more space
        self.horizontalLayout.setSpacing(0)  # Remove spacing for cleaner look
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Sidebar
        self.SideBar = QtWidgets.QWidget(self.centralwidget)
        self.SideBar.setMinimumSize(QtCore.QSize(220, 0))
        self.SideBar.setMaximumSize(QtCore.QSize(220, 1080))
        self.SideBar.setObjectName("SideBar")

        # Sidebar stylesheet - more macOS-like
        apply_sidebar_style(self.SideBar)

        # Sidebar vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SideBar)
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)  # Add some top/bottom padding
        self.verticalLayout.setSpacing(2)  # Small spacing between buttons
        self.verticalLayout.setObjectName("verticalLayout")

        # Create sidebar buttons
        self.create_sidebar_button("invoices_btn", "Invoices", ":/icons/coupon.png", "Create sales on account")
        self.create_sidebar_button("bills_btn", "Bills", ":/icons/purchase.png", "Create purchases on account")
        self.create_sidebar_button("cash_btn", "Cash", ":/icons/cash.png", "Create Receive Money or Spend Money transactions")
        self.create_sidebar_button("items_btn", "Items", ":/icons/box.png", "Manage inventory, consumables, services")
        self.create_sidebar_button("contacts_btn", "Contacts", ":/icons/people.png", "Manage contacts")
        self.create_sidebar_button("journals_btn", "Journals", ":/icons/diary.png", "Manage journal entries")
        self.create_sidebar_button("reports_btn", "Reports", ":/icons/analytics.png", "Manage reports")
        self.create_sidebar_button("settings_btn", "Settings", ":/icons/settings.png", "Manage settings")

        # Add spacer at the bottom of sidebar
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # Add sidebar to main layout
        self.horizontalLayout.addWidget(self.SideBar)

        # Content area (stacked widget)
        self.window_content = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.window_content.setSizePolicy(sizePolicy)
        self.window_content.setFrameShape(QtWidgets.QFrame.Box)
        self.window_content.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.window_content.setObjectName("window_content")

        # Add placeholder pages - useful for the dashboard
        # self.page = QtWidgets.QWidget()
        # self.page.setObjectName("page")
        # self.window_content.addWidget(self.page)

        # Add content area to main layout
        self.horizontalLayout.addWidget(self.window_content)

        # Set the central widget
        MainView.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))  # macOS menu height is typically 22px
        self.menubar.setObjectName("menubar")

        # File menu
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTitle("File")
        self.menuFile.setObjectName("menuFile")

        # Profile menu
        self.menuProfile = QtWidgets.QMenu(self.menubar)
        self.menuProfile.setTitle("Profile")
        self.menuProfile.setObjectName("menuProfile")

        MainView.setMenuBar(self.menubar)

        # Actions
        self.actionExit = QtWidgets.QAction(MainView)
        self.actionExit.setText("Exit")
        self.actionExit.setObjectName("actionExit")

        self.actionView_profile = QtWidgets.QAction(MainView)
        self.actionView_profile.setText("View profile")
        self.actionView_profile.setObjectName("actionView_profile")

        self.actionSignout = QtWidgets.QAction(MainView)
        self.actionSignout.setText("Signout")
        self.actionSignout.setObjectName("actionSignout")

        # Add actions to menus
        self.menuFile.addAction(self.actionExit)
        self.menuProfile.addAction(self.actionView_profile)
        self.menuProfile.addAction(self.actionSignout)

        # Add menus to menu bar
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProfile.menuAction())

        # Connect signals
        self.actionExit.triggered.connect(MainView.close)

        # Set window title
        MainView.setWindowTitle("Thanos")

        # Initialize the stacked widget to show the first page
        # self.window_content.setCurrentIndex(0)

        # Connect signals and slots
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def create_sidebar_button(self, object_name, text, icon_path, tooltip):
        """Helper method to create sidebar buttons with consistent styling"""
        button = QtWidgets.QPushButton(self.SideBar)
        button.setObjectName(object_name)
        button.setText(text)
        button.setToolTip(tooltip)
        button.setMinimumSize(QtCore.QSize(220, 60))

        # Set font
        font = QtGui.QFont()
        font.setBold(True)
        button.setFont(font)

        # Set icon if provided
        if icon_path:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            button.setIcon(icon)
            button.setIconSize(QtCore.QSize(24, 24))

        # Add to layout
        self.verticalLayout.addWidget(button)

        # Store the button as an attribute of self for easy access
        setattr(self, object_name, button)
