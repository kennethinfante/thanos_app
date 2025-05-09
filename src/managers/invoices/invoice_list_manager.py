import sys
from typing import List, Dict, Any
from datetime import datetime

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from sqlalchemy import and_, or_, func, column, text

from forms_py.invoice_list_view import Ui_invoiceListView

from src.managers.base_manager import BaseManager
from src.database_manager import DatabaseManager
from src.models.invoice_list_model import InvoiceListModel

from src.managers.invoices.invoice_view_manager import InvoiceViewManager

class InvoiceListManager(BaseManager):
    def __init__(self, parent=None):
        super().__init__(ui=Ui_invoiceListView(), parent=parent,
                         model=InvoiceListModel())

    def initialize_ui(self):
        self.ui.invoices_table_view.setModel(self.model)

        # # Apply column widths
        # column_widths = {
        #     0: 60,    # ID - narrow column
        #     1: 120,   # Invoice Number
        #     2: 100,   # Date
        #     3: 200,   # Customer - wider for names
        #     4: 120,   # Total Amount
        #     5: 100    # Status
        # }
        #
        # for column, width in column_widths.items():
        #     self.ui.invoices_table_view.setColumnWidth(column, width)

    def connect_signals_slots(self):
        self.ui.search_date_chbox.stateChanged.connect(self.enable_date)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.clear_btn.clicked.connect(self.clear)
        self.ui.invoices_table_view.doubleClicked.connect(self.view_invoice)
        self.ui.add_new_invoice_btn.clicked.connect(self.open_create_invoice)
        self.ui.refresh_list_btn.clicked.connect(self.refresh_list)

    def enable_date(self, state: int):
        is_enabled = state == Qt.Checked
        self.ui.from_date_edit.setEnabled(is_enabled)
        self.ui.to_date_edit.setEnabled(is_enabled)

    def search(self):
        filters = self.build_search_filters()
        self.model.update(filters)
        self.ui.invoices_table_view.update()

    def refresh_list(self):
        self.model.update()
        self.ui.invoices_table_view.update()

    def clear(self):
        self.ui.customer_lne.clear()
        self.model.update()
        self.ui.invoices_table_view.update()

    def build_search_filters(self) -> List:
        filters = []

        # Customer filter
        customer_name = self.ui.customer_lne.text().strip().lower()

        if customer_name:
            filters.append(text("LOWER(customers.name) LIKE :pattern").bindparams(
                            pattern=f"%{customer_name.lower()}%"))

        # Date range filter
        if self.ui.search_date_chbox.isChecked():
            from_date = self.ui.from_date_edit.date().toPyDate()
            to_date = self.ui.to_date_edit.date().toPyDate()
            filters.append(
                text("date BETWEEN :from_date AND :to_date")
                    .bindparams(from_date=from_date, to_date=to_date)
            )

        return filters

    def view_invoice(self, index):
        """Open the selected invoice for viewing/editing"""
        # Get the invoice ID from the first column (ID column)
        row = index.row()
        invoice_id = self.model.data(self.model.index(row, 0))

        if invoice_id:
            # Create and show the InvoiceViewManager dialog
            view_invoice_dialog = InvoiceViewManager(invoice_id, parent=self)
            # Connect the invoiceDeleted signal to refresh_list method
            view_invoice_dialog.invoiceDeleted.connect(self.refresh_list)
            view_invoice_dialog.show()


    def open_create_invoice(self):
        # create_invoice = CreateInvoice(self)
        # create_invoice.show()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    invoice_manager = InvoiceListManager()
    invoice_manager.show()
    sys.exit(app.exec_())
