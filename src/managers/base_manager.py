from PyQt5.QtWidgets import QMainWindow


class BaseManager(QMainWindow):
    """
    This class contains the basic functionality for the all the managers in the main window
    """
    def __init__(self, ui, model, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.ui.setupUi(self)
        self.model = model
        self.initialize_ui()
        self.connect_signals_slots()

    def initialize_ui(self):
        pass

    def connect_signals_slots(self):
        pass

    def build_filter(self):
        pass




    # def extract_values_from_conditions(self, conditions):
    #     placeholder = dict()
    #     for condition in conditions:
    #         placeholder[condition['column'].replace('.', '_')] = condition['value']
    #     return placeholder





