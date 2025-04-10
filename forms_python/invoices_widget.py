# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms_ui/invoices_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_invoicesWidget(object):
    def setupUi(self, invoicesWidget):
        invoicesWidget.setObjectName("invoicesWidget")
        invoicesWidget.resize(1321, 893)
        self.centralwidget = QtWidgets.QWidget(invoicesWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_date_chbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_date_chbox.setFont(font)
        self.search_date_chbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.search_date_chbox.setTristate(False)
        self.search_date_chbox.setObjectName("search_date_chbox")
        self.horizontalLayout.addWidget(self.search_date_chbox)
        self.from_date_label = QtWidgets.QLabel(self.centralwidget)
        self.from_date_label.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.from_date_label.setFont(font)
        self.from_date_label.setObjectName("from_date_label")
        self.horizontalLayout.addWidget(self.from_date_label)
        self.from_date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.from_date_edit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_date_edit.sizePolicy().hasHeightForWidth())
        self.from_date_edit.setSizePolicy(sizePolicy)
        self.from_date_edit.setMinimumSize(QtCore.QSize(160, 50))
        self.from_date_edit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.from_date_edit.setFont(font)
        self.from_date_edit.setCalendarPopup(True)
        self.from_date_edit.setDate(QtCore.QDate(2022, 1, 1))
        self.from_date_edit.setObjectName("from_date_edit")
        self.horizontalLayout.addWidget(self.from_date_edit)
        self.to_date_label = QtWidgets.QLabel(self.centralwidget)
        self.to_date_label.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.to_date_label.setFont(font)
        self.to_date_label.setObjectName("to_date_label")
        self.horizontalLayout.addWidget(self.to_date_label)
        self.to_date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.to_date_edit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_date_edit.sizePolicy().hasHeightForWidth())
        self.to_date_edit.setSizePolicy(sizePolicy)
        self.to_date_edit.setMinimumSize(QtCore.QSize(160, 50))
        self.to_date_edit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.to_date_edit.setFont(font)
        self.to_date_edit.setCalendarPopup(True)
        self.to_date_edit.setDate(QtCore.QDate(2024, 1, 1))
        self.to_date_edit.setObjectName("to_date_edit")
        self.horizontalLayout.addWidget(self.to_date_edit)
        self.invoice_num_label = QtWidgets.QLabel(self.centralwidget)
        self.invoice_num_label.setMinimumSize(QtCore.QSize(160, 50))
        self.invoice_num_label.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.invoice_num_label.setFont(font)
        self.invoice_num_label.setObjectName("invoice_num_label")
        self.horizontalLayout.addWidget(self.invoice_num_label)
        self.invoice_num_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoice_num_line_edit.sizePolicy().hasHeightForWidth())
        self.invoice_num_line_edit.setSizePolicy(sizePolicy)
        self.invoice_num_line_edit.setMinimumSize(QtCore.QSize(230, 50))
        self.invoice_num_line_edit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.invoice_num_line_edit.setObjectName("invoice_num_line_edit")
        self.horizontalLayout.addWidget(self.invoice_num_line_edit)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMinimumSize(QtCore.QSize(230, 50))
        self.search_btn.setMaximumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.add_new_invoice_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_invoice_btn.sizePolicy().hasHeightForWidth())
        self.add_new_invoice_btn.setSizePolicy(sizePolicy)
        self.add_new_invoice_btn.setMinimumSize(QtCore.QSize(230, 50))
        self.add_new_invoice_btn.setMaximumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.add_new_invoice_btn.setFont(font)
        self.add_new_invoice_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_new_invoice_btn.setObjectName("add_new_invoice_btn")
        self.verticalLayout.addWidget(self.add_new_invoice_btn)
        self.invoices_table_view = QtWidgets.QTableView(self.centralwidget)
        self.invoices_table_view.setObjectName("invoices_table_view")
        self.invoices_table_view.horizontalHeader().setDefaultSectionSize(120)
        self.invoices_table_view.horizontalHeader().setMinimumSectionSize(80)
        self.invoices_table_view.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.invoices_table_view)
        invoicesWidget.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(invoicesWidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1321, 26))
        self.menubar.setObjectName("menubar")
        invoicesWidget.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(invoicesWidget)
        self.statusbar.setObjectName("statusbar")
        invoicesWidget.setStatusBar(self.statusbar)

        self.retranslateUi(invoicesWidget)
        QtCore.QMetaObject.connectSlotsByName(invoicesWidget)

    def retranslateUi(self, invoicesWidget):
        _translate = QtCore.QCoreApplication.translate
        invoicesWidget.setWindowTitle(_translate("invoicesWidget", "Invoices widget"))
        self.search_date_chbox.setText(_translate("invoicesWidget", "Enable date"))
        self.from_date_label.setText(_translate("invoicesWidget", "From date:"))
        self.from_date_edit.setDisplayFormat(_translate("invoicesWidget", "yyyy-MM-dd"))
        self.to_date_label.setText(_translate("invoicesWidget", "To:"))
        self.to_date_edit.setDisplayFormat(_translate("invoicesWidget", "yyyy-MM-dd"))
        self.invoice_num_label.setText(_translate("invoicesWidget", "Invoice #"))
        self.search_btn.setText(_translate("invoicesWidget", "Search"))
        self.add_new_invoice_btn.setText(_translate("invoicesWidget", "Add new invoice"))
