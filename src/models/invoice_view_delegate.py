from PyQt5.QtWidgets import QStyledItemDelegate, QComboBox
from PyQt5.QtCore import Qt

class InvoiceViewDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = []
        self.accounts = []
        self.tax_rates = []

    def set_items(self, items):
        """Set the available items for the dropdown"""
        self.items = items

    def set_accounts(self, accounts):
        """Set the available accounts for the dropdown"""
        self.accounts = accounts

    def set_tax_rates(self, tax_rates):
        """Set the available tax rates for the dropdown"""
        self.tax_rates = tax_rates

    def createEditor(self, parent, option, index):
        """Create the appropriate editor for each column"""
        if index.column() == 0:  # Item column
            editor = QComboBox(parent)
            for item in self.items:
                editor.addItem(item.name, item.id)
            return editor
        elif index.column() == 1:  # Account column
            editor = QComboBox(parent)
            for account in self.accounts:
                editor.addItem(account.name, account.id)
            return editor
        elif index.column() == 5:  # Tax column
            editor = QComboBox(parent)
            for tax_rate in self.tax_rates:
                editor.addItem(f"{tax_rate.name}-{tax_rate.rate:.2f}%", tax_rate.id)
            return editor

        # For other columns, use the default editor
        return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        """Set the editor data based on the model data"""
        if index.column() in [0, 1, 5]:  # Item, Account, or Tax column
            value = index.model().data(index, Qt.EditRole)
            if value is not None:
                # Find the index of the item with the matching ID
                for i in range(editor.count()):
                    if editor.itemData(i) == value:
                        editor.setCurrentIndex(i)
                        break
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        """Set the model data based on the editor data"""
        if index.column() in [0, 1, 5]:  # Item, Account, or Tax column
            # Get the ID from the combo box
            value = editor.itemData(editor.currentIndex())
            model.setData(index, value, Qt.EditRole)
        else:
            super().setModelData(editor, model, index)