from typing import List, Dict, Any
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from src.managers.base_manager import BaseManager
from forms_py.item_list_view import Ui_itemListView
from models.items_model import ItemsModel
# from src.create_invoice import CreateInvoice


class ItemListManager(BaseManager):
    def __init__(self, parent=None):
        super().__init__(ui=Ui_itemListView(), parent=parent,
                         model=ItemsModel())

    def initialize_ui(self):
        self.ui.items_table_view.setModel(self.model)

    def connect_signals_slots(self):
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.clear_btn.clicked.connect(self.clear)
        self.ui.add_new_item_btn.clicked.connect(self.open_create_item)

    def search(self):
        filters = self.build_search_filters()
        self.model.get_items_dataframe(filters)
        self.ui.items_table_view.update()

    def clear(self):
        self.model.get_items_dataframe()
        self.ui.items_table_view.update()

    def build_search_filters(self) -> List[Dict[str, Any]]:
        conditions = []

        item_name = self.ui.item_name_line_edit.text()
        if item_name:
            conditions.append(self.build_filter('lower(name)', f"%{item_name.lower()}%", operator='like', parameter='name', connector='AND'))

        print(conditions)
        return conditions

    def open_create_item(self):
        # create_item = CreateItem(self)
        # create_item.show()

        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    item_manager = ItemListManager()
    item_manager.show()
    sys.exit(app.exec_())
