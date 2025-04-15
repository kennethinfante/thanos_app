from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from src.dao.invoice_dao import InvoiceDao

class InvoiceLinesModel(QAbstractTableModel):
    def __init__(self, invoice_id=None, parent=None):
        super().__init__(parent)
        self.dao = InvoiceDao()
        self.invoice_id = invoice_id
        self.invoice_lines = []
        self.headers = ["Item", "Account", "Description", "Quantity", "Unit Price", "Subtotal", "Tax Amount", "Line Amount"]
        self.editable_columns = [0, 1, 2, 3, 4, 6]  # Item, Account, Description, Quantity, Unit Price, Tax Amount
        self.changes = {}  # Track changes to save later

        if invoice_id:
            self.load_data()

    def load_data(self):
        """Load invoice lines for the specified invoice"""
        invoice = self.dao.get_invoice_with_lines(self.invoice_id)
        if invoice and hasattr(invoice, 'invoice_lines'):
            self.invoice_lines = invoice.invoice_lines
            self.layoutChanged.emit()
            # Clear changes when reloading data
            self.changes = {}

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

        # Check if invoice_line is None
        if invoice_line is None:
            return None

        if role == Qt.DisplayRole:
            column = index.column()

            # Handle display of item and account names
            if column == 0:  # Item
                return invoice_line.item.name if hasattr(invoice_line, 'item') and invoice_line.item else ""
            elif column == 1:  # Account
                return invoice_line.account.name if hasattr(invoice_line, 'account') and invoice_line.account else ""
            elif column == 2:  # Description
                return invoice_line.description if hasattr(invoice_line, 'description') and invoice_line.description is not None else ""
            elif column == 3:  # Quantity
                return f"{invoice_line.quantity:.2f}" if hasattr(invoice_line, 'quantity') and invoice_line.quantity is not None else "0.00"
            elif column == 4:  # Unit Price
                return f"{invoice_line.unit_price:.2f}" if hasattr(invoice_line, 'unit_price') and invoice_line.unit_price is not None else "0.00"
            elif column == 5:  # Subtotal
                # Calculate subtotal as quantity * unit_price
                quantity = invoice_line.quantity if hasattr(invoice_line, 'quantity') and invoice_line.quantity is not None else 0
                unit_price = invoice_line.unit_price if hasattr(invoice_line, 'unit_price') and invoice_line.unit_price is not None else 0
                subtotal = quantity * unit_price
                return f"{subtotal:.2f}"
            elif column == 6:  # Tax Amount
                return f"{invoice_line.tax_amount:.2f}" if hasattr(invoice_line, 'tax_amount') and invoice_line.tax_amount is not None else "0.00"
            elif column == 7:  # Line Amount
                # Calculate line amount as subtotal + tax_amount
                quantity = invoice_line.quantity if hasattr(invoice_line, 'quantity') and invoice_line.quantity is not None else 0
                unit_price = invoice_line.unit_price if hasattr(invoice_line, 'unit_price') and invoice_line.unit_price is not None else 0
                subtotal = quantity * unit_price
                tax_amount = invoice_line.tax_amount if hasattr(invoice_line, 'tax_amount') and invoice_line.tax_amount is not None else 0
                line_amount = subtotal + tax_amount
                return f"{line_amount:.2f}"

        elif role == Qt.EditRole:
            column = index.column()

            if column == 0:  # Item
                return invoice_line.item_id if hasattr(invoice_line, 'item_id') else None
            elif column == 1:  # Account
                return invoice_line.account_id if hasattr(invoice_line, 'account_id') else None
            elif column == 2:  # Description
                return invoice_line.description if hasattr(invoice_line, 'description') else ""
            elif column == 3:  # Quantity
                return invoice_line.quantity if hasattr(invoice_line, 'quantity') else 0
            elif column == 4:  # Unit Price
                return invoice_line.unit_price if hasattr(invoice_line, 'unit_price') else 0
            elif column == 6:  # Tax Amount
                return invoice_line.tax_amount if hasattr(invoice_line, 'tax_amount') else 0

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return None

    def flags(self, index):
        """Define which cells are editable"""
        if not index.isValid():
            return Qt.NoItemFlags

        # Make specific columns editable
        if index.column() in self.editable_columns:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setData(self, index, value, role=Qt.EditRole):
        """Handle editing of cells"""
        if not index.isValid() or role != Qt.EditRole:
            return False

        row = index.row()
        col = index.column()

        if not (0 <= row < len(self.invoice_lines)):
            return False

        invoice_line = self.invoice_lines[row]
        line_id = invoice_line.id

        # Track changes for later saving
        if line_id not in self.changes:
            self.changes[line_id] = {}

        try:
            if col == 0:  # Item
                # This would typically involve selecting an item from a dropdown
                # For now, we'll just store the item ID
                self.changes[line_id]['item_id'] = value if value else None
                invoice_line.item_id = value if value else None
            elif col == 1:  # Account
                # This would typically involve selecting an account from a dropdown
                # For now, we'll just store the account ID
                self.changes[line_id]['account_id'] = value if value else None
                invoice_line.account_id = value if value else None
            elif col == 2:  # Description
                self.changes[line_id]['description'] = str(value)
                invoice_line.description = str(value)
            elif col == 3:  # Quantity
                quantity = float(value)
                self.changes[line_id]['quantity'] = quantity
                invoice_line.quantity = quantity

                # Update subtotal (calculated field)
                subtotal = quantity * invoice_line.unit_price
                invoice_line.subtotal = subtotal
                self.changes[line_id]['subtotal'] = subtotal

                # Update line amount (calculated field)
                line_amount = subtotal + invoice_line.tax_amount
                invoice_line.line_amount = line_amount
                self.changes[line_id]['line_amount'] = line_amount
            elif col == 4:  # Unit Price
                unit_price = float(value)
                self.changes[line_id]['unit_price'] = unit_price
                invoice_line.unit_price = unit_price

                # Update subtotal (calculated field)
                subtotal = invoice_line.quantity * unit_price
                invoice_line.subtotal = subtotal
                self.changes[line_id]['subtotal'] = subtotal

                # Update line amount (calculated field)
                line_amount = subtotal + invoice_line.tax_amount
                invoice_line.line_amount = line_amount
                self.changes[line_id]['line_amount'] = line_amount
            elif col == 6:  # Tax Amount
                tax_amount = float(value)
                self.changes[line_id]['tax_amount'] = tax_amount
                invoice_line.tax_amount = tax_amount

                # Update line amount (calculated field)
                subtotal = invoice_line.quantity * invoice_line.unit_price
                line_amount = subtotal + tax_amount
                invoice_line.line_amount = line_amount
                self.changes[line_id]['line_amount'] = line_amount
            else:
                return False

            # Emit dataChanged for the entire row to update all calculated fields
            self.dataChanged.emit(self.index(row, 0), self.index(row, self.columnCount() - 1))
            return True

        except (ValueError, TypeError) as e:
            print(f"Error setting data: {e}")
            return False

    def save_all_changes(self):
        """Save all changes to the database"""
        for line_id, changes in self.changes.items():
            if changes:  # Only update if there are changes
                self.dao.update_invoice_line(line_id, changes)

        # Clear changes after saving
        self.changes = {}

        # Recalculate invoice totals
        if self.invoice_id:
            self.dao.recalculate_invoice_totals(self.invoice_id)

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