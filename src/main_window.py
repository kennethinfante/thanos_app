import sys, os, importlib

from PyQt5.QtWidgets import QApplication, QMainWindow
from forms_py.main_window import Ui_MainWindow
from src.database_manager import DatabaseManager

from src.managers.invoices.invoice_list_manager import InvoiceListManager
# from src.managers.bills_manager import BillsManager
# from src.managers.cash_manager import CashManager
# from src.managers.items.items_manager import ItemListManager
# from src.managers.contacts_manager import ContactsManager
# from src.managers.journals_manager import JournalsManager
# from src.managers.reports_manager import ReportsManager
# from settings_manager import SettingsManager
# from system_properties import SystemProperties

# from dashboard import Dashboard


class AppMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AppMainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_database()
        self.initializePages()
        self.connect_signals_slots()
        self.ui.window_content.setCurrentIndex(0)

    def connect_signals_slots(self):
        self.ui.invoices_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["invoices_manager"]["index"]))
        # self.ui.bills_btn.clicked.connect(
        #     lambda: self.change_widget(self.widgets["bills_manager"]["index"]))
        # self.ui.cash_btn.clicked.connect(
        #     lambda: self.change_widget(self.widgets["cash_manager"]["index"]))
        # self.ui.items_btn.clicked.connect(
        #     lambda: self.change_widget(self.widgets["items_manager"]["index"]))
        # self.ui.contacts_btn.clicked.connect(
        #     lambda: self.change_widget(self.widgets["contacts_manager"]["index"]))
        # self.ui.journals_btn.clicked.connect(
        #     lambda: self.change_widget(self.widgets["journals_manager"]["index"]))
        # self.ui.reports_btn.clicked.connect(
        #     lambda: self.change_widget(self.widgets["reports_manager"]["index"]))
        # self.ui.settings_btn.clicked.connect(
        #     lambda: self.change_widget(self.widgets["settings_manager"]["index"]))

    def load_data_objects(self):
        """Dynamically import all data objects from the do folder"""
        do_path = os.path.join(os.path.dirname(__file__), 'do')
        do_modules = []

        # Get all Python files in the do directory
        for file in os.listdir(do_path):
            if file.endswith('.py') and file != '__init__.py':
                module_name = file[:-3]  # Remove .py extension
                try:
                    # Import the module dynamically
                    module = importlib.import_module(f'src.do.{module_name}')
                    do_modules.append(module)
                    print(f"Loaded data object: {module_name}")
                except ImportError as e:
                    print(f"Failed to import {module_name}: {e}")

        return do_modules

    def initialize_database(self):
        """Initialize the database schema"""
        db_manager = DatabaseManager()

        # Load all data objects dynamically
        self.data_objects = self.load_data_objects()

        # Create all tables
        db_manager.Base.metadata.create_all(db_manager.engine)

        print("Database schema created successfully")

    def initializePages(self):
        self.widgets = {
            "invoices_manager":
                {"index": 1, "widget": InvoiceListManager()}
            # "bills_manager":
            #     {"index": 2, "widget": BillsManager()},
            # "cash_manager":
            #     {"index": 3, "widget": CashManager()},
            # "items_manager":
            #     {"index": 4, "widget": ItemListManager()},
            # 'contacts_manager':
            #     {"index": 5, "widget": ContactsManager()},
            # "journals_manager":
            #     {"index": 6, "widget": JournalsManager()},
            # "reports_manager":
            #     {"index": 7, "widget": ReportsManager()},
            # "settings_manager":
            #     {"index": 8, "widget": SettingsManager()}
        }
        [self.ui.window_content.insertWidget(self.widgets[widget]["index"], self.widgets[widget]["widget"]) for widget in self.widgets]


    def change_widget(self, index):
        """
        Change the stacked widget to the widget at index
        :param index:Integer represents the widget's index in the stacked widget
        :return: None
        """
        self.ui.window_content.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppMainWindow()
    window.show()
    sys.exit(app.exec_())