from typing import List, Dict, Any
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from src.managers.base_manager import BaseManager
from forms_python.invoices_widget import Ui_invoicesWidget
from models.invoices_model import InvoicesModel
# from src.create_invoice import CreateInvoice


class InvoicesManager(BaseManager):
    def __init__(self, parent=None):
        super().__init__(ui=Ui_invoicesWidget(), parent=parent,
                                              model=InvoicesModel())

    def initialize_ui(self):
        self.ui.invoices_table_view.setModel(self.model)

    def connect_signals_slots(self):
        self.ui.search_date_chbox.stateChanged.connect(self.enable_date)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.add_new_invoice_btn.clicked.connect(self.open_create_invoice)

    def enable_date(self, state: int):
        is_enabled = state == Qt.Checked
        self.ui.from_date_edit.setEnabled(is_enabled)
        self.ui.to_date_edit.setEnabled(is_enabled)

    def search(self):
        conditions = self.build_search_filters()
        self.model.get_invoice_dataframe(conditions)
        self.ui.invoices_table_view.update()

    def build_search_filters(self) -> List[Dict[str, Any]]:
        conditions = []
        if self.ui.search_date_chbox.isChecked():
            conditions.extend([
                self.build_filter('date', self.ui.from_date_edit.text(), '>=', parameter='from_date'),
                self.build_filter('date', self.ui.to_date_edit.text(), '<=', parameter='to_date', connector='AND')
            ])

        invoice_num = self.ui.invoice_num_line_edit.text()
        if invoice_num:
            conditions.append(self.build_filter('invoice_number', invoice_num, connector='AND'))

        return conditions

    def open_create_invoice(self):
        # create_invoice = CreateInvoice(self)
        # create_invoice.show()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    invoice_manager = InvoicesManager()
    invoice_manager.show()
    sys.exit(app.exec_())
