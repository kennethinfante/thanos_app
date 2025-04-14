from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from sqlalchemy import desc

from src.database_manager import DatabaseManager
from src.do.invoice import Invoice

class InvoicesModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db_manager = DatabaseManager()
        self.session = self.db_manager.Session()
        self.invoices = []
        self.headers = ["ID", "Invoice Number", "Date", "Customer", "Total Amount", "Status"]
        self.load_data()

    def load_data(self, filters=None):
        query = self.session.query(Invoice)

        if filters:
            for filter_condition in filters:
                query = query.filter(filter_condition)

        self.invoices = query.order_by(desc(Invoice.date)).all()
        self.layoutChanged.emit()

    def rowCount(self, parent=QModelIndex()):
        return len(self.invoices)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.invoices)):
            return None

        invoice = self.invoices[index.row()]

        if role == Qt.DisplayRole:
            if index.column() == 0:
                return invoice.id
            elif index.column() == 1:
                return invoice.invoice_number
            elif index.column() == 2:
                return invoice.date.strftime("%Y-%m-%d")
            elif index.column() == 3:
                return invoice.customer.name if invoice.customer else ""
            elif index.column() == 4:
                return f"{invoice.total_amount:.2f}"
            elif index.column() == 5:
                return invoice.status

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return None

    def update(self, filters=None):
        self.load_data(filters)