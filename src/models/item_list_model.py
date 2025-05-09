from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex

from src.dao.item_dao import ItemDao

class ItemListModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dao = ItemDao()
        self.items = []
        self.headers = ["ID", "Name", "Sale Price", "Purchase Price", "Inventory Tracking", "Is Consumable", "Is Service"]
        self.load_data()

    def load_data(self, filters=None):
        self.items = self.dao.get_all_items(filters)
        self.layoutChanged.emit()

    # retained to differentiate between initial load and data update
    def update(self, filters=None):
        self.load_data(filters)

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.items)):
            return None

        item = self.items[index.row()]

        if role == Qt.DisplayRole:
            # Define column mappings with formatting functions
            # ["ID", "Name", "Sale Price", "Purchase Price", "Inventory Tracking", "Is Consumable", "Is Service"]
            column_mappings = {
                0: lambda item: item.id,
                1: lambda item: item.name,
                2: lambda item: item.sale_price,
                3: lambda item: item.purchase_price,
                4: lambda item: "True" if item.inventory_tracking else "False",
                5: lambda item: "True" if item.is_consumable else "False",
                6: lambda item: "True" if item.is_service else "False"
            }

            # Return formatted data if column is in our mappings
            if index.column() in column_mappings:
                return column_mappings[index.column()](item)

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return None

    def get_column_widths(self):
        """
        Returns a dictionary with recommended column widths for each column
        """
        # ["ID", "Name", "Sale Price", "Purchase Price", "Inventory Tracking", "Is Consumable", "Is Service"]
        return {
            0: 60,    # ID - narrow column
            1: 200,   # Name
            2: 100,   # Sale Price
            3: 100,   # Purchase Price
            4: 60,   # tracked
            5: 60,   # consumed
            6: 60,   # service
        }
