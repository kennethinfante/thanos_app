import resources_rc
from .form_styles import *

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
        self.central_widget = QtWidgets.QWidget(MainView)
        self.central_widget.setObjectName("central_widget")

        # Main horizontal layout
        self.main_hlayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.main_hlayout.setContentsMargins(0, 0, 0, 0)  # Remove margins for more space
        self.main_hlayout.setSpacing(0)  # Remove spacing for cleaner look
        self.main_hlayout.setObjectName("main_hlayout")

        # Navigation Sidebar
        self.nav_sidebar = QtWidgets.QWidget(self.central_widget)
        self.nav_sidebar.setMinimumSize(QtCore.QSize(220, 0))
        self.nav_sidebar.setMaximumSize(QtCore.QSize(220, 1080))
        self.nav_sidebar.setObjectName("nav_sidebar")

        # Sidebar stylesheet - more macOS-like
        apply_sidebar_style(self.nav_sidebar)

        # Sidebar vertical layout
        self.nav_vlayout = QtWidgets.QVBoxLayout(self.nav_sidebar)
        self.nav_vlayout.setContentsMargins(0, 10, 0, 10)  # Add some top/bottom padding
        self.nav_vlayout.setSpacing(2)  # Small spacing between buttons
        self.nav_vlayout.setObjectName("nav_vlayout")

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
        self.nav_vlayout.addItem(spacerItem)

        # Add sidebar to main layout
        self.main_hlayout.addWidget(self.nav_sidebar)

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
        self.main_hlayout.addWidget(self.window_content)

        # Set the central widget
        MainView.setCentralWidget(self.central_widget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))  # macOS menu height is typically 22px
        self.menubar.setObjectName("menubar")

        # Create menus using the helper method
        self.create_menu(self.menubar, "menu_file", "File")
        self.create_menu(self.menubar, "menu_profile", "Profile")

        MainView.setMenuBar(self.menubar)

        # Actions
        self.create_menu_action(
            MainView, "action_exit", "Exit",
            tooltip="Exit the application",
            shortcut="Ctrl+Q",
            slot=MainView.close
        )

        self.create_menu_action(
            MainView, "action_view_profile", "View profile",
            tooltip="View your profile information"
        )

        self.create_menu_action(
            MainView, "action_signout", "Sign out",
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

    def create_sidebar_button(self, object_name, text, icon_path=None, tooltip=None):
        """Helper method to create sidebar buttons with consistent styling"""
        button = QtWidgets.QPushButton(self.nav_sidebar)
        button.setObjectName(object_name)
        button.setText(text)
        button.setMinimumSize(QtCore.QSize(220, 60))

        if tooltip:
            button.setToolTip(tooltip)

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
        self.nav_vlayout.addWidget(button)

        # Store the button as an attribute of self for easy access
        setattr(self, object_name, button)


    def create_menu(self, parent, object_name, title):
        """Helper method to create menus with consistent styling

        Parameters:
        -----------
        parent : QMenuBar
            The parent menu bar
        object_name : str
            The object name for the menu
        title : str
            The display title for the menu

        Returns:
        --------
        None: The object_name is attached to self
        """

        menu = QtWidgets.QMenu(parent)
        menu.setObjectName(object_name)
        menu.setTitle(title)

        # Store the menu as an attribute of self for easy access
        setattr(self, object_name, menu)

        return menu

    def create_menu_action(self, parent, object_name, text, tooltip=None, shortcut=None, icon_path=None, slot=None):
        """Helper method to create menu actions with consistent styling

        Parameters:
        -----------
        parent : QWidget
            The parent widget for the action (usually MainView)
        object_name : str
            The object name for the action
        text : str
            The display text for the action
        tooltip : str, optional
            The tooltip text for the action
        shortcut : str, optional
            Keyboard shortcut for the action (e.g., "Ctrl+Q")
        icon_path : str, optional
            Path to the icon for the action
        slot : function, optional
            Function to connect to the triggered signal

        Returns:
        --------
        None: The object_name is attached to self
        """

        action = QtWidgets.QAction(parent)
        action.setObjectName(object_name)
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

        # Store the action as an attribute of self for easy access
        setattr(self, object_name, action)
