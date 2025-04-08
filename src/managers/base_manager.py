from PyQt5.QtWidgets import QMainWindow


class BaseManager(QMainWindow):
    """
    This class contains the basic functionality for the all the managers in the main window
    """
    def __init__(self, ui, model, parent=None):
        super(BaseManager, self).__init__(parent)
        self.ui = ui
        self.ui.setupUi(self)
        self.model = model
        self.initialize_ui()
        self.connect_signals_slots()

    def build_conditions(self, conditions):
        """
        This function builds conditions for the SELECT query, based on whether the required widget has something in it
        or not
        :return:
        """
        return ' WHERE ' + ' '.join([self.get_condition_string(condition) for condition in conditions]) if any(conditions) else ""

    def build_condition(self, column, value, operator, options='', logic=''):
        return {
            'column': column,
            'value': value,
            'operator': operator,
            'options': options,
            'logic': logic
        }

    def extract_values_from_conditions(self, conditions):
        placeholder = dict()
        for condition in conditions:
            placeholder[condition['column'].replace('.', '_')] = condition['value']
        return placeholder

    def get_condition_string(self, condition):
        """
        Get a condition string out of a condition object
        :param condition: A condition object contains the required parameters for the condition
        :return: A condition string to be used in SQL query
        """
        return f"{condition['column']} {condition['operator']} :{condition['column'].replace('.', '_')} {condition['options']} {condition['logic']}"

    def initialize_ui(self):
        self.setup_table()

    def connect_signals_slots(self):
        pass

    def search(self):
        pass

    def setup_table(self):
        pass
