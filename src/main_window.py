import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from forms_python.main_window import Ui_MainWindow
from src.managers.employees_manager import EmployeesManager
from system_properties import SystemProperties
from src.managers.customers_manager import CustomersManager
from src.managers.products_manager import ProductsManager
from src.managers.category_manager import CategoriesManager
from src.managers.brands_manager import BrandsManager
from src.managers.invoices_manager import InvoicesManager
from dashboard import Dashboard


class AppMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AppMainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initializePages()
        self.connect_signals_slots()
        self.ui.window_content.setCurrentIndex(0)

    def connect_signals_slots(self):
        self.ui.employees_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["employees_manager"]["index"]))
        self.ui.system_properties_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["system_properties"]["index"]))
        self.ui.customers_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["customers_manager"]["index"]))
        self.ui.categories_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["categories_manager"]["index"])
        )
        self.ui.brands_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["brands_manager"]["index"]))
        self.ui.products_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["products_manager"]["index"]))
        self.ui.invoices_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["invoices_manager"]["index"]))

    def initializePages(self):
        self.widgets = {
            "dashboard":
                {"index": 0, "widget": Dashboard()},
            "system_properties":
                {"index": 1, "widget": SystemProperties()},
            "employees_manager":
                {"index": 2, "widget": EmployeesManager()},
            "customers_manager":
                {"index": 3, "widget": CustomersManager()},
            'categories_manager':
                {"index": 4, "widget": CategoriesManager()},
            "brands_manager":
                {"index": 5, "widget": BrandsManager()},
            "products_manager":
                {"index": 6, "widget": ProductsManager()},
            "invoices_manager":
                {"index": 7, "widget": InvoicesManager()}
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