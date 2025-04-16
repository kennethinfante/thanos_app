from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from src.dao.invoice_dao import InvoiceDao

class InvoiceLinesModel(QAbstractTableModel):
    def __init__(self, invoice_id=None, parent=None):
        super().__init__(parent)
        self.dao = InvoiceDao()
        self.invoice_id = invoice_id
        self.invoice_lines = []
        self.headers = ["Item", "Account", "Description", "Quantity", "Unit Price", "Tax", "Subtotal", "Tax Amount", "Line Amount"]
        self.editable_columns = [0, 1, 2, 3, 4, 5]  # Item, Account, Description, Quantity, Unit Price, Tax
        self.changes = {}  # Track changes to save later
        self.new_lines = []  # Track new lines to be added
        self.deleted_line_ids = []  # Track lines to be deleted

        if invoice_id:
            self.load_data()

    def load_data(self):
        """Load invoice lines for the specified invoice"""
        invoice = self.dao.get_invoice_with_lines(self.invoice_id)
        if invoice and hasattr(invoice, 'invoice_lines'):
            # Make sure relationships are loaded
            self.invoice_lines = []
            for line in invoice.invoice_lines:
                # Ensure item, account, and tax_rate are loaded
                if hasattr(line, 'item_id') and line.item_id:
                    line.item = self.dao.get_item_by_id(line.item_id)
                if hasattr(line, 'account_id') and line.account_id:
                    line.account = self.dao.get_account_by_id(line.account_id)
                if hasattr(line, 'tax_rate_id') and line.tax_rate_id:
                    line.tax_rate = self.dao.get_tax_rate(line.tax_rate_id)
                self.invoice_lines.append(line)

            self.layoutChanged.emit()
            # Clear all tracking when reloading data
            self.changes = {}
            self.new_lines = []
            self.deleted_line_ids = []

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
                # If item_id is None, return empty string to represent blank option
                if not hasattr(invoice_line, 'item_id') or invoice_line.item_id is None:
                    return ""

                # If item is not loaded, try to load it
                if not hasattr(invoice_line, 'item') or invoice_line.item is None:
                    invoice_line.item = self.dao.get_item_by_id(invoice_line.item_id)

                return invoice_line.item.name if hasattr(invoice_line, 'item') and invoice_line.item else ""

            elif column == 1:  # Account
                # If account_id is None, return empty string to represent blank option
                if not hasattr(invoice_line, 'account_id') or invoice_line.account_id is None:
                    return ""

                # If account is not loaded, try to load it
                if not hasattr(invoice_line, 'account') or invoice_line.account is None:
                    invoice_line.account = self.dao.get_account_by_id(invoice_line.account_id)

                return invoice_line.account.name if hasattr(invoice_line, 'account') and invoice_line.account else ""
            elif column == 2:  # Description
                return invoice_line.description if hasattr(invoice_line, 'description') and invoice_line.description is not None else ""
            elif column == 3:  # Quantity
                return f"{invoice_line.quantity:.2f}" if hasattr(invoice_line, 'quantity') and invoice_line.quantity is not None else "0.00"
            elif column == 4:  # Unit Price
                return f"{invoice_line.unit_price:.2f}" if hasattr(invoice_line, 'unit_price') and invoice_line.unit_price is not None else "0.00"
            elif column == 5:  # Tax
                # If tax_rate is not loaded, try to load it
                if not hasattr(invoice_line, 'tax_rate') or invoice_line.tax_rate is None:
                    if hasattr(invoice_line, 'tax_rate_id') and invoice_line.tax_rate_id:
                        invoice_line.tax_rate = self.dao.get_tax_rate(invoice_line.tax_rate_id)

                tax_rate = invoice_line.tax_rate if hasattr(invoice_line, 'tax_rate') and invoice_line.tax_rate else None
                if tax_rate:
                    return f"{tax_rate.name}-{tax_rate.rate:.2f}%"
                return ""

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
                # Store the original value to check validation later
                original_item_id = invoice_line.item_id

                # Set the new value
                if value == "" or value is None:
                    self.changes[line_id]['item_id'] = None
                    invoice_line.item_id = None
                    invoice_line.item = None
                else:
                    self.changes[line_id]['item_id'] = value
                    invoice_line.item_id = value
                    invoice_line.item = None  # Clear for reload

                # Validate: either item or account must be specified
                if invoice_line.item_id is None and invoice_line.account_id is None:
                    # Revert to original value
                    invoice_line.item_id = original_item_id
                    if line_id in self.changes:
                        if 'item_id' in self.changes[line_id]:
                            del self.changes[line_id]['item_id']
                    return False

            elif col == 1:  # Account
                # Store the original value to check validation later
                original_account_id = invoice_line.account_id

                # Set the new value
                if value == "" or value is None:
                    self.changes[line_id]['account_id'] = None
                    invoice_line.account_id = None
                    invoice_line.account = None
                else:
                    self.changes[line_id]['account_id'] = value
                    invoice_line.account_id = value
                    invoice_line.account = None  # Clear for reload

                # Validate: either item or account must be specified
                if invoice_line.item_id is None and invoice_line.account_id is None:
                    # Revert to original value
                    invoice_line.account_id = original_account_id
                    if line_id in self.changes:
                        if 'account_id' in self.changes[line_id]:
                            del self.changes[line_id]['account_id']
                    return False
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
            elif col == 5:  # Tax Rate
                # Store the tax rate ID
                self.changes[line_id]['tax_rate_id'] = value if value else None
                invoice_line.tax_rate_id = value if value else None

                # Update tax amount based on the new tax rate
                # Get the tax rate percentage
                tax_rate = self.dao.get_tax_rate(value) if value else None
                tax_percentage = tax_rate.rate if tax_rate else 0

                # Calculate tax amount
                subtotal = invoice_line.quantity * invoice_line.unit_price
                tax_amount = subtotal * (tax_percentage / 100)
                invoice_line.tax_amount = tax_amount
                self.changes[line_id]['tax_amount'] = tax_amount

                # Update line amount
                line_amount = subtotal + tax_amount
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
        # First, save changes to existing lines
        for line_id, changes in self.changes.items():
            if changes and line_id not in self.deleted_line_ids:  # Only update if there are changes and not marked for deletion
                self.dao.update_invoice_line(line_id, changes)

        # Add new lines
        for new_line in self.new_lines:
            line_data = {
                'invoice_id': self.invoice_id,
                'description': new_line.description,
                'quantity': new_line.quantity,
                'unit_price': new_line.unit_price,
                'tax_amount': new_line.tax_amount,
                'subtotal': new_line.subtotal,
                'line_amount': new_line.line_amount,
                'item_id': new_line.item_id,
                'account_id': new_line.account_id,
                'tax_rate_id': new_line.tax_rate_id
            }
            self.dao.add_invoice_line(line_data)

        # Delete lines marked for deletion
        for line_id in self.deleted_line_ids:
            self.dao.delete_invoice_line(line_id)

        # Clear all tracking lists
        self.changes = {}
        self.new_lines = []
        self.deleted_line_ids = []

        # Recalculate invoice totals
        if self.invoice_id:
            self.dao.recalculate_invoice_totals(self.invoice_id)

        # Reload data to get fresh state from database
        self.load_data()

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

    # adding or removing lines locally
    def add_line_locally(self):
        """Add a new line to the model without saving to database"""
        # Create a temporary negative ID to identify new lines
        temp_id = -1 * (len(self.new_lines) + 1)

        # Create a new line object with default values
        from src.do.invoice import InvoiceLine  # Import at the top of the file in practice
        new_line = InvoiceLine(
            id=temp_id,
            invoice_id=self.invoice_id,
            description="New Line Item",
            quantity=1.0,
            unit_price=0.0,
            tax_amount=0.0,
            subtotal=0.0,
            line_amount=0.0,
            item_id=None,
            account_id=None,
            tax_rate_id=None
        )

        # Add to our tracking list
        self.new_lines.append(new_line)

        # Add to the displayed lines
        self.beginInsertRows(QModelIndex(), len(self.invoice_lines), len(self.invoice_lines))
        self.invoice_lines.append(new_line)
        self.endInsertRows()

        return True

    def remove_line_locally(self, row):
        """Mark a line for deletion without removing from database"""
        if 0 <= row < len(self.invoice_lines):
            line = self.invoice_lines[row]

            # If it's a new line (with negative ID), just remove it from our lists
            if line.id < 0:
                # Find and remove from new_lines
                for i, new_line in enumerate(self.new_lines):
                    if new_line.id == line.id:
                        self.new_lines.pop(i)
                        break
            else:
                # Otherwise, mark for deletion
                self.deleted_line_ids.append(line.id)

                # Remove any pending changes for this line
                if line.id in self.changes:
                    del self.changes[line.id]

            # Remove from the displayed lines
            self.beginRemoveRows(QModelIndex(), row, row)
            self.invoice_lines.pop(row)
            self.endRemoveRows()

            return True
        return False

    # for dropdowns
    def get_available_items(self):
        """Get all available items for dropdown with a blank option"""
        items = self.dao.get_all_items()
        # Add a blank option at the beginning
        blank_item = type('BlankItem', (), {'id': None, 'name': ''})()
        return [blank_item] + items

    def get_available_accounts(self):
        """Get all available accounts for dropdown with a blank option"""
        accounts = self.dao.get_all_accounts()
        # Add a blank option at the beginning
        blank_account = type('BlankAccount', (), {'id': None, 'name': ''})()
        return [blank_account] + accounts

    def get_available_tax_rates(self):
        """Get all available tax rates for dropdown"""
        return self.dao.get_all_tax_rates()