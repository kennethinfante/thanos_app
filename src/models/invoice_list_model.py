from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex

from src.dao.invoice_dao import InvoiceDao

class InvoiceListModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dao = InvoiceDao()
        self.invoices = []
        self.headers = ["ID", "Invoice Number", "Date", "Customer", "Total Amount", "Status"]
        self.load_data()

    def load_data(self, filters=None):
        self.invoices = self.dao.get_all_invoices(filters)
        self.layoutChanged.emit()

    # retained to differentiate between initial load and data update
    def update(self, filters=None):
        self.load_data(filters)

    def rowCount(self, parent=QModelIndex()):
        return len(self.invoices)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.invoices)):
            return None

        invoice = self.invoices[index.row()]

        if role == Qt.DisplayRole:
            # Define column mappings with formatting functions
            column_mappings = {
                0: lambda inv: inv.id,
                1: lambda inv: inv.invoice_number,
                2: lambda inv: inv.date.strftime("%Y-%m-%d"),
                3: lambda inv: inv.customer.name if inv.customer else "",
                4: lambda inv: f"{inv.total_amount:.2f}",
                5: lambda inv: inv.status
            }

            # Return formatted data if column is in our mappings
            if index.column() in column_mappings:
                return column_mappings[index.column()](invoice)

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return None