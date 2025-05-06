from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_invoiceView(object):
    def setupUi(self, invoiceView):
        # Main window setup
        invoiceView.setObjectName("invoiceView")
        invoiceView.setWindowModality(QtCore.Qt.ApplicationModal)
        # Recommended size for 15-inch MacBook Pro with Retina display
        invoiceView.resize(1200, 800)
        invoiceView.setMinimumSize(QtCore.QSize(1200, 800))
        
        # Central widget
        self.centralwidget = QtWidgets.QWidget(invoiceView)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main vertical layout for the entire form
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setObjectName("main_layout")
        
        # Header section
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setObjectName("header_layout")
        
        # Left side of header (customer, dates)
        self.header_form = QtWidgets.QFormLayout()
        self.header_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.header_form.setObjectName("header_form")
        
        # Customer selection
        self.customer_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.customer_label.setFont(font)
        self.customer_label.setText("Customer")
        self.customer_label.setObjectName("customer_label")
        self.header_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.customer_label)
        
        self.customer_cb = QtWidgets.QComboBox(self.centralwidget)
        self.customer_cb.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customer_cb.setFont(font)
        self.customer_cb.setObjectName("customer_cb")
        self.header_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.customer_cb)
        
        # Invoice date
        self.invoice_date_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.invoice_date_label.setFont(font)
        self.invoice_date_label.setText("Invoice date")
        self.invoice_date_label.setObjectName("invoice_date_label")
        self.header_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.invoice_date_label)
        
        self.invoice_date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.invoice_date_edit.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.invoice_date_edit.setFont(font)
        self.invoice_date_edit.setCalendarPopup(True)
        self.invoice_date_edit.setDate(QtCore.QDate(2025, 1, 1))
        self.invoice_date_edit.setDisplayFormat("d/M/yyyy")
        self.invoice_date_edit.setObjectName("invoice_date_edit")
        self.header_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.invoice_date_edit)
        
        # Due date
        self.due_date_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.due_date_label.setFont(font)
        self.due_date_label.setText("Due Date")
        self.due_date_label.setObjectName("due_date_label")
        self.header_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.due_date_label)
        
        self.due_date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.due_date_edit.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.due_date_edit.setFont(font)
        self.due_date_edit.setCalendarPopup(True)
        self.due_date_edit.setDate(QtCore.QDate(2025, 1, 31))
        self.due_date_edit.setDisplayFormat("d/M/yyyy")
        self.due_date_edit.setObjectName("due_date_edit")
        self.header_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.due_date_edit)
        
        self.header_layout.addLayout(self.header_form)
        
        # Spacer between left and right header
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header_layout.addItem(spacer_item)
        
        # Right side of header (invoice number, add client button)
        self.header_vbox = QtWidgets.QVBoxLayout()
        self.header_vbox.setObjectName("header_vbox")
        
        self.invoice_number_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.invoice_number_label.setFont(font)
        self.invoice_number_label.setText("Invoice #")
        self.invoice_number_label.setObjectName("invoice_number_label")
        self.header_vbox.addWidget(self.invoice_number_label)
        
        self.add_client_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_client_btn.setEnabled(False)
        self.add_client_btn.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.add_client_btn.setFont(font)
        self.add_client_btn.setText("Create new customer")
        self.add_client_btn.setObjectName("add_client_btn")
        self.header_vbox.addWidget(self.add_client_btn)
        
        self.header_layout.addLayout(self.header_vbox)
        self.main_layout.addLayout(self.header_layout)
        
        # Add/Remove line buttons
        self.add_remove_hbox = QtWidgets.QHBoxLayout()
        self.add_remove_hbox.setObjectName("add_remove_hbox")
        
        self.add_line_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_line_btn.setMinimumSize(QtCore.QSize(115, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.add_line_btn.setFont(font)
        self.add_line_btn.setText("Add Line")
        self.add_line_btn.setObjectName("add_line_btn")
        self.add_remove_hbox.addWidget(self.add_line_btn)
        
        self.remove_line_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_line_btn.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.remove_line_btn.setFont(font)
        self.remove_line_btn.setText("Remove Line")
        self.remove_line_btn.setObjectName("remove_line_btn")
        self.add_remove_hbox.addWidget(self.remove_line_btn)
        
        # Add spacer to push buttons to the left
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.add_remove_hbox.addItem(spacer_item2)
        
        self.main_layout.addLayout(self.add_remove_hbox)
        
        # Invoice lines table
        self.invoice_lines_table_view = QtWidgets.QTableView(self.centralwidget)
        self.invoice_lines_table_view.setMinimumHeight(400)  # Ensure table has enough height
        self.invoice_lines_table_view.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed |
                                                     QtWidgets.QAbstractItemView.DoubleClicked |
                                                     QtWidgets.QAbstractItemView.EditKeyPressed |
                                                     QtWidgets.QAbstractItemView.SelectedClicked)
        self.invoice_lines_table_view.setObjectName("invoice_lines_table_view")
        self.invoice_lines_table_view.horizontalHeader().setCascadingSectionResizes(True)
        self.invoice_lines_table_view.horizontalHeader().setStretchLastSection(True)
        self.main_layout.addWidget(self.invoice_lines_table_view)
        
        # Totals section
        self.totals_layout = QtWidgets.QHBoxLayout()
        self.totals_layout.setObjectName("totals_layout")
        
        # Add spacer to push totals to the right
        spacer_item3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.totals_layout.addItem(spacer_item3)
        
        # Invoice totals form
        self.invoice_total_form = QtWidgets.QFormLayout()
        self.invoice_total_form.setObjectName("invoice_total_form")
        
        # Subtotal
        self.subtotal_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.subtotal_label.setFont(font)
        self.subtotal_label.setText("Subtotal")
        self.subtotal_label.setObjectName("subtotal_label")
        self.invoice_total_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.subtotal_label)
        
        self.subtotal_amt_label = QtWidgets.QLabel(self.centralwidget)
        self.subtotal_amt_label.setMinimumWidth(150)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.subtotal_amt_label.setFont(font)
        self.subtotal_amt_label.setAutoFillBackground(True)
        self.subtotal_amt_label.setText("")
        self.subtotal_amt_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.subtotal_amt_label.setObjectName("subtotal_amt_label")
        self.invoice_total_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.subtotal_amt_label)
        
        # Tax
        self.tax_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.tax_label.setFont(font)
        self.tax_label.setText("Tax")
        self.tax_label.setObjectName("tax_label")
        self.invoice_total_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tax_label)
        
        self.tax_amt_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.tax_amt_label.setFont(font)
        self.tax_amt_label.setAutoFillBackground(True)
        self.tax_amt_label.setText("")
        self.tax_amt_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.tax_amt_label.setObjectName("tax_amt_label")
        self.invoice_total_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tax_amt_label)
        
        # Total
        self.total_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.total_label.setFont(font)
        self.total_label.setText("Total")
        self.total_label.setObjectName("total_label")
        self.invoice_total_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.total_label)
        
        self.total_amt_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.total_amt_label.setFont(font)
        self.total_amt_label.setAutoFillBackground(True)
        self.total_amt_label.setText("")
        self.total_amt_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.total_amt_label.setObjectName("total_amt_label")
        self.invoice_total_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.total_amt_label)
        
        self.totals_layout.addLayout(self.invoice_total_form)
        self.main_layout.addLayout(self.totals_layout)
        
        # Action buttons (Delete, Save, Cancel)
        self.btn_hbox = QtWidgets.QHBoxLayout()
        self.btn_hbox.setObjectName("btn_hbox")
        
        # Delete button
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setMinimumSize(QtCore.QSize(115, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.delete_btn.setFont(font)
        self.delete_btn.setStyleSheet("QPushButton { color: rgb(255, 85, 0) }")
        self.delete_btn.setText("Delete")
        self.delete_btn.setObjectName("delete_btn")
        self.btn_hbox.addWidget(self.delete_btn)

        # Add spacer to push Save and Cancel buttons to the right
        spacer_item4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn_hbox.addItem(spacer_item4)

        # Save button
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setMinimumSize(QtCore.QSize(115, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.save_btn.setFont(font)
        self.save_btn.setText("Save")
        self.save_btn.setObjectName("save_btn")
        self.btn_hbox.addWidget(self.save_btn)

        # Cancel button
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setMinimumSize(QtCore.QSize(115, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.setObjectName("cancel_btn")
        self.btn_hbox.addWidget(self.cancel_btn)

        # Add the action buttons layout to the main layout
        self.main_layout.addLayout(self.btn_hbox)

        # Set the central widget
        invoiceView.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(invoiceView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        invoiceView.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(invoiceView)
        self.statusbar.setObjectName("statusbar")
        invoiceView.setStatusBar(self.statusbar)

        # Set window title
        invoiceView.setWindowTitle("Invoice")

        # Connect signals
        # Note: We're not connecting cancel_btn.clicked to invoiceView.close here
        # because it should be handled in the manager class
        QtCore.QMetaObject.connectSlotsByName(invoiceView)