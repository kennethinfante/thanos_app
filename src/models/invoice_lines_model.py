from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from src.dao.invoice_dao import InvoiceDao

class InvoiceLinesModel(QAbstractTableModel):
    def __init__(self, invoice_id=None, parent=None):
        super().__init__(parent)
        self.dao = InvoiceDao()
        self.invoice_id = invoice_id
        self.invoice_lines = []
        self.headers = ["Item", "Account", "Description", "Quantity", "Unit Price", "Subtotal", "Tax Amount", "Line Amount"]
        if invoice_id:
            self.load_data()

    def load_data(self):
        """Load invoice lines for the specified invoice"""
        invoice = self.dao.get_invoice_by_id(self.invoice_id)
        if invoice and hasattr(invoice, 'invoice_lines'):
            self.invoice_lines = invoice.invoice_lines
            self.layoutChanged.emit()

    def set_invoice_id(self, invoice_id):
        """Set the invoice ID and reload data"""
        self.invoice_id = invoice_id
        self.load_data()

    def rowCount(self, parent=QModelIndex()):
        return len(self.invoice_lines)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.invoice_lines)):
            return None

        invoice_line = self.invoice_lines[index.row()]

        if role == Qt.DisplayRole:
            # Define column mappings with formatting functions
            column_mappings = {
                0: lambda line: line.item.name if line.item else "",
                1: lambda line: line.account.name if line.account else "",
                2: lambda line: line.description,
                3: lambda line: f"{line.quantity:.2f}",
                4: lambda line: f"{line.unit_price:.2f}",
                5: lambda line: f"{line.subtotal:.2f}",
                6: lambda line: f"{line.tax_amount:.2f}",
                7: lambda line: f"{line.line_amount:.2f}"
            }

            # Return formatted data if column is in our mappings
            if index.column() in column_mappings:
                return column_mappings[index.column()](invoice_line)

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return None

    def add_line(self, line_data):
        """Add a new line to the invoice"""
        # This would typically call a DAO method to add a line
        # For now, we'll just reload the data
        self.load_data()

    def update_line(self, line_id, line_data):
        """Update an existing line"""
        # This would typically call a DAO method to update a line
        # For now, we'll just reload the data
        self.load_data()

    def delete_line(self, line_id):
        """Delete a line from the invoice"""
        # This would typically call a DAO method to delete a line
        # For now, we'll just reload the data
        self.load_data()