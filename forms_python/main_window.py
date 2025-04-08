# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms_ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(10000, 10000))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(" QWidget#SideBar\n"
" {\n"
"            background-color: white;\n"
"            margin: 0\n"
" }\n"
"QPushButton{\n"
"  background-color: #838383;\n"
"  border: none;\n"
"  color: black;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #585858;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(54, 54, 54);\n"
"}\n"
"\n"
"QHeaderView{\n"
"background-color: #838383;\n"
"  border: none;\n"
"  color: black;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SideBar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.SideBar.sizePolicy().hasHeightForWidth())
        self.SideBar.setSizePolicy(sizePolicy)
        self.SideBar.setMinimumSize(QtCore.QSize(200, 0))
        self.SideBar.setMaximumSize(QtCore.QSize(250, 16777215))
        self.SideBar.setStyleSheet("  QPushButton\n"
"            { \n"
"                background-color: #FFFFFF;\n"
"                color: rgb(190, 190, 190);\n"
"                border: none;\n"
"                color: white;\n"
"                text-align: left;\n"
"                text-decoration: none;\n"
"                color: black;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover{\n"
"                background-color: grey;\n"
"            }\n"
"            QPushButton:hover:pressed{\n"
"                background-color: #bebebe;\n"
"            }")
        self.SideBar.setObjectName("SideBar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SideBar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.invoices_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(218)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoices_btn.sizePolicy().hasHeightForWidth())
        self.invoices_btn.setSizePolicy(sizePolicy)
        self.invoices_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.invoices_btn.setFont(font)
        self.invoices_btn.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/coupon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.invoices_btn.setIcon(icon)
        self.invoices_btn.setIconSize(QtCore.QSize(24, 24))
        self.invoices_btn.setObjectName("invoices_btn")
        self.verticalLayout.addWidget(self.invoices_btn)
        self.bills_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bills_btn.sizePolicy().hasHeightForWidth())
        self.bills_btn.setSizePolicy(sizePolicy)
        self.bills_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.bills_btn.setFont(font)
        self.bills_btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/purchase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bills_btn.setIcon(icon1)
        self.bills_btn.setIconSize(QtCore.QSize(24, 24))
        self.bills_btn.setObjectName("bills_btn")
        self.verticalLayout.addWidget(self.bills_btn)
        self.cash_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cash_btn.sizePolicy().hasHeightForWidth())
        self.cash_btn.setSizePolicy(sizePolicy)
        self.cash_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.cash_btn.setFont(font)
        self.cash_btn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/cash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cash_btn.setIcon(icon2)
        self.cash_btn.setIconSize(QtCore.QSize(24, 24))
        self.cash_btn.setObjectName("cash_btn")
        self.verticalLayout.addWidget(self.cash_btn)
        self.items_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.items_btn.sizePolicy().hasHeightForWidth())
        self.items_btn.setSizePolicy(sizePolicy)
        self.items_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.items_btn.setFont(font)
        self.items_btn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/box.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.items_btn.setIcon(icon3)
        self.items_btn.setIconSize(QtCore.QSize(24, 24))
        self.items_btn.setObjectName("items_btn")
        self.verticalLayout.addWidget(self.items_btn)
        self.contacts_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contacts_btn.sizePolicy().hasHeightForWidth())
        self.contacts_btn.setSizePolicy(sizePolicy)
        self.contacts_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.contacts_btn.setFont(font)
        self.contacts_btn.setAutoFillBackground(False)
        self.contacts_btn.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/people.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.contacts_btn.setIcon(icon4)
        self.contacts_btn.setIconSize(QtCore.QSize(24, 24))
        self.contacts_btn.setObjectName("contacts_btn")
        self.verticalLayout.addWidget(self.contacts_btn)
        self.journals_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.journals_btn.sizePolicy().hasHeightForWidth())
        self.journals_btn.setSizePolicy(sizePolicy)
        self.journals_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.journals_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.journals_btn.setFont(font)
        self.journals_btn.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/diary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.journals_btn.setIcon(icon5)
        self.journals_btn.setIconSize(QtCore.QSize(24, 24))
        self.journals_btn.setObjectName("journals_btn")
        self.verticalLayout.addWidget(self.journals_btn)
        self.reports_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reports_btn.sizePolicy().hasHeightForWidth())
        self.reports_btn.setSizePolicy(sizePolicy)
        self.reports_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.reports_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.reports_btn.setFont(font)
        self.reports_btn.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/analytics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reports_btn.setIcon(icon6)
        self.reports_btn.setIconSize(QtCore.QSize(24, 24))
        self.reports_btn.setObjectName("reports_btn")
        self.verticalLayout.addWidget(self.reports_btn)
        self.settings_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.settings_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.settings_btn.setFont(font)
        self.settings_btn.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon7)
        self.settings_btn.setIconSize(QtCore.QSize(24, 24))
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout.addWidget(self.settings_btn)
        self.horizontalLayout.addWidget(self.SideBar)
        self.window_content = QtWidgets.QStackedWidget(self.centralwidget)
        self.window_content.setFrameShape(QtWidgets.QFrame.Box)
        self.window_content.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.window_content.setObjectName("window_content")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.window_content.addWidget(self.page)
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.window_content.addWidget(self.widget)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.window_content.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.window_content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuProfile = QtWidgets.QMenu(self.menubar)
        self.menuProfile.setObjectName("menuProfile")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionView_profile = QtWidgets.QAction(MainWindow)
        self.actionView_profile.setObjectName("actionView_profile")
        self.actionSignout = QtWidgets.QAction(MainWindow)
        self.actionSignout.setObjectName("actionSignout")
        self.menuFile.addAction(self.actionExit)
        self.menuProfile.addAction(self.actionView_profile)
        self.menuProfile.addAction(self.actionSignout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProfile.menuAction())

        self.retranslateUi(MainWindow)
        self.window_content.setCurrentIndex(0)
        self.actionExit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.invoices_btn.setToolTip(_translate("MainWindow", "Create sales on account"))
        self.invoices_btn.setText(_translate("MainWindow", "Invoices"))
        self.bills_btn.setToolTip(_translate("MainWindow", "Create purchases on account"))
        self.bills_btn.setText(_translate("MainWindow", "Bills"))
        self.cash_btn.setToolTip(_translate("MainWindow", "Create Receive Money or Spend Money transactions"))
        self.cash_btn.setText(_translate("MainWindow", "Cash"))
        self.items_btn.setToolTip(_translate("MainWindow", "Manage inventory, consumables, services"))
        self.items_btn.setText(_translate("MainWindow", "Items"))
        self.contacts_btn.setToolTip(_translate("MainWindow", "Manage contacts"))
        self.contacts_btn.setText(_translate("MainWindow", "Contacts"))
        self.journals_btn.setToolTip(_translate("MainWindow", "Manage journal entries"))
        self.journals_btn.setText(_translate("MainWindow", "Journals"))
        self.reports_btn.setToolTip(_translate("MainWindow", "Manage reports"))
        self.reports_btn.setText(_translate("MainWindow", "Reports"))
        self.settings_btn.setToolTip(_translate("MainWindow", "Manage settings"))
        self.settings_btn.setText(_translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuProfile.setTitle(_translate("MainWindow", "Profile"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionView_profile.setText(_translate("MainWindow", "View profile"))
        self.actionSignout.setText(_translate("MainWindow", "Signout"))
import resources_rc
