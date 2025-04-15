import sys
from typing import List, Dict, Any
from datetime import datetime

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from sqlalchemy import and_, or_, func, column, text

from src.database_manager import DatabaseManager
from src.models.invoices_model import InvoicesModel

from forms_python.invoices_view import Ui_invoicesView

from src.managers.base_manager import BaseManager
from src.managers.invoices.view_invoice import ViewInvoice

class InvoicesManager(BaseManager):
    def __init__(self, parent=None):
        super().__init__(ui=Ui_invoicesView(), parent=parent,
                         model=InvoicesModel())

    def initialize_ui(self):
        self.ui.invoices_table_view.setModel(self.model)

        self.ui.invoices_table_view.setColumnWidth(0, 100)
        self.ui.invoices_table_view.setColumnWidth(1, 150)
        self.ui.invoices_table_view.setColumnWidth(2, 100)
        self.ui.invoices_table_view.setColumnWidth(3, 200)
        self.ui.invoices_table_view.setColumnWidth(4, 150)
        self.ui.invoices_table_view.setColumnWidth(5, 100)

    def connect_signals_slots(self):
        self.ui.search_date_chbox.stateChanged.connect(self.enable_date)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.clear_btn.clicked.connect(self.clear)
        self.ui.invoices_table_view.doubleClicked.connect(self.view_invoice)
        self.ui.add_new_invoice_btn.clicked.connect(self.open_create_invoice)

    def enable_date(self, state: int):
        is_enabled = state == Qt.Checked
        self.ui.from_date_edit.setEnabled(is_enabled)
        self.ui.to_date_edit.setEnabled(is_enabled)

    def search(self):
        filters = self.build_search_filters()
        self.model.update(filters)
        self.ui.invoices_table_view.update()

    def clear(self):
        self.ui.customer_line_edit.clear()
        self.model.update()
        self.ui.invoices_table_view.update()

    def build_search_filters(self) -> List:
        filters = []

        # Customer filter
        customer_name = self.ui.customer_line_edit.text().strip().lower()

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
            # Create and show the ViewInvoice dialog
            view_invoice_dialog = ViewInvoice(invoice_id, parent=self)
            view_invoice_dialog.show()


    def open_create_invoice(self):
        # create_invoice = CreateInvoice(self)
        # create_invoice.show()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    invoice_manager = InvoicesManager()
    invoice_manager.show()
    sys.exit(app.exec_())