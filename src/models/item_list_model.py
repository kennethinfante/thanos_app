from typing import List, Dict, Any
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from src.dao.item_dao import ItemDao


class ItemListModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.item_dao = ItemDao()
        self.item_dataframe = pd.DataFrame()
        self.get_items_dataframe()

    def get_items_dataframe(self, conditions: List[Dict[str, Any]] = None):
        self.item_dataframe = self.item_dao.get_items_dataframe(conditions)
        self.layoutChanged.emit()

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.item_dataframe)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.item_dataframe.columns)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return str(self.item_dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return str(self.item_dataframe.columns[section])

        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return str(self.item_dataframe.index[section])

        return None
