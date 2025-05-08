import resources_rc
from .form_styles import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainView(object):
    def setupUi(self, MainView):
        # Main window setup
        MainView.setObjectName("MainView")
        # # Appropriate size for MacBook Pro 2015 with Retina display
        MainView.resize(1440, 900)
        # MainView.setMinimumSize(QtCore.QSize(1024, 768)) # aspect ratio is 1.6
        MainView.setMinimumSize(QtCore.QSize(1600, 1000))
        MainView.setMaximumSize(QtCore.QSize(1920, 1080))

        # Base stylesheet - more macOS-like
        apply_main_window_style(MainView)

        # Central widget
        self.central_widget = QtWidgets.QWidget(MainView)
        self.central_widget.setObjectName("central_widget")

        # Main horizontal layout
        self.main_hly = QtWidgets.QHBoxLayout(self.central_widget)
        self.main_hly.setContentsMargins(0, 0, 0, 0)  # Remove margins for more space
        self.main_hly.setSpacing(0)  # Remove spacing for cleaner look
        self.main_hly.setObjectName("main_hly")

        # Navigation Sidebar
        self.sidebar = QtWidgets.QWidget(self.central_widget)
        self.sidebar.setMinimumSize(QtCore.QSize(220, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(220, 1080))
        self.sidebar.setObjectName("sidebar")

        # Sidebar stylesheet - more macOS-like
        apply_sidebar_style(self.sidebar)

        # Sidebar vertical layout
        self.sidebar_vly = QtWidgets.QVBoxLayout(self.sidebar)
        self.sidebar_vly.setContentsMargins(0, 10, 0, 10)  # Add some top/bottom padding
        self.sidebar_vly.setSpacing(2)  # Small spacing between buttons
        self.sidebar_vly.setObjectName("sidebar_vly")

        # Create sidebar buttons
        self.invoices_btn = self.create_sidebar_button("Invoices", ":/icons/coupon.png", "Create sales on account")
        self.bills_btn = self.create_sidebar_button("Bills", ":/icons/purchase.png", "Create purchases on account")
        self.cash_btn = self.create_sidebar_button("Cash", ":/icons/cash.png",
                                                   "Create Receive Money or Spend Money transactions")
        self.items_btn = self.create_sidebar_button("Items", ":/icons/box.png",
                                                    "Manage inventory, consumables, services")
        self.contacts_btn = self.create_sidebar_button("Contacts", ":/icons/people.png", "Manage contacts")
        self.journals_btn = self.create_sidebar_button("Journals", ":/icons/diary.png", "Manage journal entries")
        self.reports_btn = self.create_sidebar_button("Reports", ":/icons/analytics.png", "Manage reports")
        self.settings_btn = self.create_sidebar_button("Settings", ":/icons/settings.png", "Manage settings")

        sidebar_buttons = [self.invoices_btn, self.bills_btn, self.cash_btn, self.items_btn, self.contacts_btn,
                           self.journals_btn, self.reports_btn, self.settings_btn]

        for button in sidebar_buttons:
            self.sidebar_vly.addWidget(button)

        # Add spacer at the bottom of sidebar
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebar_vly.addItem(spacerItem)

        # Add sidebar to main layout
        self.main_hly.addWidget(self.sidebar)

        # Content area (stacked widget)
        self.window_content = QtWidgets.QStackedWidget(self.central_widget)
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
        self.main_hly.addWidget(self.window_content)

        # Set the central widget
        MainView.setCentralWidget(self.central_widget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))  # macOS menu height is typically 22px
        self.menubar.setObjectName("menubar")

        # Create menus using the helper method
        self.menu_file = self.create_menu(self.menubar, "menu_file", "File")
        self.menu_profile = self.create_menu(self.menubar, "menu_profile", "Profile")

        MainView.setMenuBar(self.menubar)

        # Actions
        self.action_exit = self.create_menu_action(
            MainView, "Exit",
            tooltip="Exit the application",
            shortcut="Ctrl+Q",
            slot=MainView.close
        )

        self.action_view_profile = self.create_menu_action(
            MainView, "View profile",
            tooltip="View your profile information"
        )

        self.action_signout = self.create_menu_action(
            MainView, "Sign out",
            tooltip="Sign out of your account"
        )

        # Add actions to menus
        self.menu_file.addAction(self.action_exit)
        self.menu_profile.addAction(self.action_view_profile)
        self.menu_profile.addAction(self.action_signout)

        # Add menus to menu bar
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_profile.menuAction())

        # Connect signals
        self.action_exit.triggered.connect(MainView.close)

        # Set window title
        MainView.setWindowTitle("Thanos")

        # Initialize the stacked widget to show the first page
        # self.window_content.setCurrentIndex(0)

        # Connect signals and slots
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def create_sidebar_button(self, text, icon_path=None, tooltip=None, object_name=None):
        """Helper method to create sidebar buttons with consistent styling"""
        button = QtWidgets.QPushButton(self.sidebar)
        button.setText(text)
        button.setMinimumSize(QtCore.QSize(220, 60))

        if tooltip:
            button.setToolTip(tooltip)
        if object_name:
            button.setObjectName(object_name)

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

        return button

    def create_menu(self, parent, title, object_name=None):
        """Helper method to create menus with consistent styling

        Args:
            parent : The parent menu bar
            title : The display title for the menu
            object_name : The object name for the menu (optional)


        Returns:
            QMenu: The created menu
        """

        menu = QtWidgets.QMenu(parent)
        menu.setTitle(title)

        if object_name:
            menu.setObjectName(object_name)

        return menu

    def create_menu_action(self, parent, text, tooltip=None, shortcut=None, icon_path=None, slot=None,
                           object_name=None):
        """Helper method to create menu actions with consistent styling

        Args:
            parent : The parent widget for the action (usually MainView)
            object_name : The object name for the action
            text : The display text for the action
            tooltip : The tooltip text for the action (optional)
            shortcut : Keyboard shortcut for the action (e.g., "Ctrl+Q") (optional)
            icon_path : Path to the icon for the action (optional)
            slot : Function to connect to the triggered signal (optional)

        Returns:
            QAction: The created menu action
        """

        action = QtWidgets.QAction(parent)
        action.setText(text)

        if tooltip:
            action.setToolTip(tooltip)

        if shortcut:
            action.setShortcut(shortcut)

        if icon_path:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            action.setIcon(icon)

        if slot:
            action.triggered.connect(slot)

        if object_name:
            action.setObjectName(object_name)

        return action
