from PyQt5.QtCore import QModelIndex, QAbstractTableModel, QVariant, Qt
from src.dao.invoice_dao import InvoiceDao
from src.logger import Logger


class InvoicesModel(QAbstractTableModel):
    def __init__(self):
        super(InvoicesModel, self).__init__()
        self.invoice_dao = InvoiceDao()
        self.invoice_dataframe = None
        self.get_invoice_dataframe()

    def rowCount(self, parent=QModelIndex()):
        return self.invoice_dataframe.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return len(self.invoice_dataframe.columns)

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole and len(self.invoice_dataframe.columns) > 0:
            return self.invoice_dataframe.columns[section]

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            return str(self.invoice_dataframe.iat[index.row(), index.column()])
        return QVariant()

    def get_invoice_dataframe(self, conditions=None):
        self.invoice_dataframe = self.invoice_dao.get_invoices_dataframe(conditions=conditions)
        self.dataChanged.emit(QModelIndex(), QModelIndex())
        print(self.invoice_dataframe)
        return self.invoice_dataframe
