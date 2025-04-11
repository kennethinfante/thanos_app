from typing import List, Dict, Any
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from src.dao.invoice_dao import InvoiceDao


class InvoicesModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.invoice_dao = InvoiceDao()
        self.invoice_dataframe = pd.DataFrame()
        self.get_invoice_dataframe()

    def get_invoice_dataframe(self, conditions: List[Dict[str, Any]] = None):
        self.invoice_dataframe = self.invoice_dao.get_invoices_dataframe(conditions)
        self.layoutChanged.emit()

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.invoice_dataframe)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.invoice_dataframe.columns)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return str(self.invoice_dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return str(self.invoice_dataframe.columns[section])

        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return str(self.invoice_dataframe.index[section])

        return None
