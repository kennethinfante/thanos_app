import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from forms_python.main_window import Ui_MainWindow
from src.managers.invoices_manager import InvoicesManager
# from src.managers.bills_manager import BillsManager
# from src.managers.cash_manager import CashManager
# from src.managers.items_manager import ItemsManager
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
        self.initializePages()
        self.connect_signals_slots()
        self.ui.window_content.setCurrentIndex(0)

    def connect_signals_slots(self):
        self.ui.sales_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["invoices_manager"]["index"]))
        # self.ui.purchases_btn.clicked.connect(
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

    def initializePages(self):
        # index starts at the bottom
        self.widgets = {
            # "dashboard":
            #     {"index": 0, "widget": Dashboard()},
            # "settings_manager":
            #     {"index": 1, "widget": SettingsManager()},
            # "reports_manager":
            #     {"index": 2, "widget": ReportsManager()},
            # "journals_manager":
            #     {"index": 3, "widget": JournalsManager()},
            # 'contacts_manager':
            #     {"index": 4, "widget": ContactsManager()},
            # "items_manager":
            #     {"index": 5, "widget": ItemsManager()},
            # "cash_manager":
            #     {"index": 6, "widget": CashManager()},
            # "bills_manager":
            #     {"index": 7, "widget": BillsManager()},
            "invoices_manager":
                {"index": 8, "widget": InvoicesManager()}
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