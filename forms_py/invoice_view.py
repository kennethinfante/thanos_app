# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms_ui/invoice_view2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_invoiceView(object):
    def setupUi(self, invoiceView):
        invoiceView.setObjectName("invoiceView")
        invoiceView.setWindowModality(QtCore.Qt.ApplicationModal)
        invoiceView.resize(1200, 1000)
        invoiceView.setMinimumSize(QtCore.QSize(1200, 1000))
        invoiceView.setMaximumSize(QtCore.QSize(1200, 1000))
        self.centralwidget = QtWidgets.QWidget(invoiceView)
        self.centralwidget.setObjectName("centralwidget")
        self.invoice_lines_table_view = QtWidgets.QTableView(self.centralwidget)
        self.invoice_lines_table_view.setGeometry(QtCore.QRect(20, 220, 1150, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoice_lines_table_view.sizePolicy().hasHeightForWidth())
        self.invoice_lines_table_view.setSizePolicy(sizePolicy)
        self.invoice_lines_table_view.setMinimumSize(QtCore.QSize(0, 0))
        self.invoice_lines_table_view.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.invoice_lines_table_view.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.invoice_lines_table_view.setObjectName("invoice_lines_table_view")
        self.invoice_lines_table_view.horizontalHeader().setCascadingSectionResizes(True)
        self.invoice_lines_table_view.horizontalHeader().setStretchLastSection(True)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(23, 890, 1141, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.btn_hbox = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.btn_hbox.setContentsMargins(0, 0, 0, 0)
        self.btn_hbox.setObjectName("btn_hbox")
        self.delete_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.delete_btn.setMinimumSize(QtCore.QSize(115, 50))
        self.delete_btn.setMaximumSize(QtCore.QSize(115, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.delete_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setAutoFillBackground(False)
        self.delete_btn.setStyleSheet("QPushButton { \n"
"    color : rgb(255, 85, 0)\n"
"}")
        self.delete_btn.setObjectName("delete_btn")
        self.btn_hbox.addWidget(self.delete_btn)
        spacerItem = QtWidgets.QSpacerItem(1100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn_hbox.addItem(spacerItem)
        self.save_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.save_btn.setMinimumSize(QtCore.QSize(115, 50))
        self.save_btn.setMaximumSize(QtCore.QSize(115, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setAutoFillBackground(True)
        self.save_btn.setObjectName("save_btn")
        self.btn_hbox.addWidget(self.save_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.cancel_btn.setMinimumSize(QtCore.QSize(115, 50))
        self.cancel_btn.setMaximumSize(QtCore.QSize(115, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.btn_hbox.addWidget(self.cancel_btn)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(25, 11, 611, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.header_form = QtWidgets.QFormLayout(self.layoutWidget1)
        self.header_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.header_form.setContentsMargins(0, 0, 0, 0)
        self.header_form.setObjectName("header_form")
        self.customer_cb = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_cb.sizePolicy().hasHeightForWidth())
        self.customer_cb.setSizePolicy(sizePolicy)
        self.customer_cb.setMinimumSize(QtCore.QSize(300, 30))
        self.customer_cb.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.customer_cb.setFont(font)
        self.customer_cb.setObjectName("customer_cb")
        self.header_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.customer_cb)
        self.customer_label = QtWidgets.QLabel(self.layoutWidget1)
        self.customer_label.setMinimumSize(QtCore.QSize(120, 25))
        self.customer_label.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.customer_label.setFont(font)
        self.customer_label.setObjectName("customer_label")
        self.header_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.customer_label)
        self.invoice_date_label = QtWidgets.QLabel(self.layoutWidget1)
        self.invoice_date_label.setMinimumSize(QtCore.QSize(190, 20))
        self.invoice_date_label.setMaximumSize(QtCore.QSize(190, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.invoice_date_label.setFont(font)
        self.invoice_date_label.setObjectName("invoice_date_label")
        self.header_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.invoice_date_label)
        self.invoice_date_edit = QtWidgets.QDateEdit(self.layoutWidget1)
        self.invoice_date_edit.setMinimumSize(QtCore.QSize(300, 30))
        self.invoice_date_edit.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.invoice_date_edit.setFont(font)
        self.invoice_date_edit.setCalendarPopup(True)
        self.invoice_date_edit.setDate(QtCore.QDate(2025, 1, 1))
        self.invoice_date_edit.setObjectName("invoice_date_edit")
        self.header_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.invoice_date_edit)
        self.due_date_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.due_date_label.setFont(font)
        self.due_date_label.setObjectName("due_date_label")
        self.header_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.due_date_label)
        self.due_date_edit = QtWidgets.QDateEdit(self.layoutWidget1)
        self.due_date_edit.setMinimumSize(QtCore.QSize(300, 30))
        self.due_date_edit.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.due_date_edit.setFont(font)
        self.due_date_edit.setCalendarPopup(True)
        self.due_date_edit.setDate(QtCore.QDate(2025, 1, 31))
        self.due_date_edit.setObjectName("due_date_edit")
        self.header_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.due_date_edit)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(880, 10, 291, 131))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.header_vbox = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.header_vbox.setContentsMargins(0, 0, 0, 0)
        self.header_vbox.setObjectName("header_vbox")
        self.invoice_number_label = QtWidgets.QLabel(self.layoutWidget2)
        self.invoice_number_label.setMinimumSize(QtCore.QSize(250, 25))
        self.invoice_number_label.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.invoice_number_label.setFont(font)
        self.invoice_number_label.setObjectName("invoice_number_label")
        self.header_vbox.addWidget(self.invoice_number_label)
        self.add_client_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.add_client_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_client_btn.sizePolicy().hasHeightForWidth())
        self.add_client_btn.setSizePolicy(sizePolicy)
        self.add_client_btn.setMinimumSize(QtCore.QSize(200, 30))
        self.add_client_btn.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_client_btn.setFont(font)
        self.add_client_btn.setObjectName("add_client_btn")
        self.header_vbox.addWidget(self.add_client_btn)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 160, 274, 52))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.add_remove_hbox = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.add_remove_hbox.setContentsMargins(0, 0, 0, 0)
        self.add_remove_hbox.setObjectName("add_remove_hbox")
        self.add_line_btn = QtWidgets.QPushButton(self.layoutWidget3)
        self.add_line_btn.setMinimumSize(QtCore.QSize(115, 50))
        self.add_line_btn.setMaximumSize(QtCore.QSize(115, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_line_btn.setFont(font)
        self.add_line_btn.setObjectName("add_line_btn")
        self.add_remove_hbox.addWidget(self.add_line_btn)
        self.remove_line_btn = QtWidgets.QPushButton(self.layoutWidget3)
        self.remove_line_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.remove_line_btn.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remove_line_btn.setFont(font)
        self.remove_line_btn.setObjectName("remove_line_btn")
        self.add_remove_hbox.addWidget(self.remove_line_btn)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(894, 750, 271, 121))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.invoice_total_form = QtWidgets.QFormLayout(self.layoutWidget4)
        self.invoice_total_form.setContentsMargins(0, 0, 0, 0)
        self.invoice_total_form.setObjectName("invoice_total_form")
        self.subtotal_label = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subtotal_label.setFont(font)
        self.subtotal_label.setObjectName("subtotal_label")
        self.invoice_total_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.subtotal_label)
        self.subtotal_amt_label = QtWidgets.QLabel(self.layoutWidget4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.subtotal_amt_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subtotal_amt_label.setFont(font)
        self.subtotal_amt_label.setAutoFillBackground(True)
        self.subtotal_amt_label.setText("")
        self.subtotal_amt_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subtotal_amt_label.setObjectName("subtotal_amt_label")
        self.invoice_total_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.subtotal_amt_label)
        self.tax_label = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tax_label.setFont(font)
        self.tax_label.setObjectName("tax_label")
        self.invoice_total_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tax_label)
        self.tax_amt_label = QtWidgets.QLabel(self.layoutWidget4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tax_amt_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tax_amt_label.setFont(font)
        self.tax_amt_label.setAutoFillBackground(True)
        self.tax_amt_label.setText("")
        self.tax_amt_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tax_amt_label.setObjectName("tax_amt_label")
        self.invoice_total_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tax_amt_label)
        self.total_label = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.total_label.setFont(font)
        self.total_label.setObjectName("total_label")
        self.invoice_total_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.total_label)
        self.total_amt_label = QtWidgets.QLabel(self.layoutWidget4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.total_amt_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.total_amt_label.setFont(font)
        self.total_amt_label.setAutoFillBackground(True)
        self.total_amt_label.setText("")
        self.total_amt_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_amt_label.setObjectName("total_amt_label")
        self.invoice_total_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.total_amt_label)
        invoiceView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(invoiceView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        invoiceView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(invoiceView)
        self.statusbar.setObjectName("statusbar")
        invoiceView.setStatusBar(self.statusbar)

        self.retranslateUi(invoiceView)
        self.cancel_btn.clicked.connect(invoiceView.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(invoiceView)

    def retranslateUi(self, invoiceView):
        _translate = QtCore.QCoreApplication.translate
        invoiceView.setWindowTitle(_translate("invoiceView", "MainWindow"))
        self.delete_btn.setText(_translate("invoiceView", "Delete"))
        self.save_btn.setText(_translate("invoiceView", "Save"))
        self.cancel_btn.setText(_translate("invoiceView", "Cancel"))
        self.customer_label.setText(_translate("invoiceView", "Customer"))
        self.invoice_date_label.setText(_translate("invoiceView", "Invoice date"))
        self.invoice_date_edit.setDisplayFormat(_translate("invoiceView", "d/M/yyyy"))
        self.due_date_label.setText(_translate("invoiceView", "Due Date"))
        self.due_date_edit.setDisplayFormat(_translate("invoiceView", "d/M/yyyy"))
        self.invoice_number_label.setText(_translate("invoiceView", "Invoice #"))
        self.add_client_btn.setText(_translate("invoiceView", "Create new customer"))
        self.add_line_btn.setText(_translate("invoiceView", "Add Line"))
        self.remove_line_btn.setText(_translate("invoiceView", "Remove Line"))
        self.subtotal_label.setText(_translate("invoiceView", "Subtotal"))
        self.tax_label.setText(_translate("invoiceView", "Tax"))
        self.total_label.setText(_translate("invoiceView", "Total"))
