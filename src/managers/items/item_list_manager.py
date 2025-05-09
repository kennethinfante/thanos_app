import sys
from typing import List, Dict, Any
from datetime import datetime

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from sqlalchemy import and_, or_, func, column, text

from forms_py.item_list_view import Ui_itemListView

from src.managers.base_manager import BaseManager
from src.database_manager import DatabaseManager
from src.models.item_list_model import ItemListModel

# from src.managers.items.item_view_manager import ItemViewManager
from src.utils.table_utils import *

class ItemListManager(BaseManager):
    def __init__(self, parent=None):
        super().__init__(ui=Ui_itemListView(), parent=parent,
                         model=ItemListModel())

    def initialize_ui(self):
        self.ui.items_table_view.setModel(self.model)
        # Apply column widths
        apply_column_widths(self.ui.items_table_view, self.model)

    def connect_signals_slots(self):
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.clear_btn.clicked.connect(self.clear)
        self.ui.items_table_view.doubleClicked.connect(self.view_item)
        self.ui.add_new_item_btn.clicked.connect(self.open_create_item)

    def search(self):
        filters = self.build_search_filters()
        self.model.update(filters)
        self.ui.items_table_view.update()

    def clear(self):
        self.ui.item_name_lne.clear()
        self.model.update()
        self.ui.items_table_view.update()

    def build_search_filters(self) -> List:
        filters = []

        # Customer filter
        item_name = self.ui.item_name_lne.text().strip().lower()

        if item_name:
            filters.append(text("LOWER(customers.name) LIKE :pattern").bindparams(
                            pattern=f"%{item_name.lower()}%"))

        return filters

    def view_item(self, index):
        # """Open the selected item for viewing/editing"""
        # # Get the item ID from the first column (ID column)
        # row = index.row()
        # item_id = self.model.data(self.model.index(row, 0))

        # if item_id:
        #     # Create and show the itemViewManager dialog
        #     view_item_dialog =ItemViewManager(item_id, parent=self)
        #     # Connect the itemDeleted signal to refresh_list method
        #     view_item_dialog.itemDeleted.connect(self.refresh_list)
        #     view_item_dialog.show()

        pass


    def open_create_item(self):
        # create_item = CreateItem(self)
        # create_item.show()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    item_manager = ItemListManager()
    item_manager.show()
    sys.exit(app.exec_())
