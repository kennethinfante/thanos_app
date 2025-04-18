from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex, pyqtSignal
from src.dao.invoice_dao import InvoiceDao
from src.dao.item_dao import ItemDao
from src.dao.account_dao import AccountDao
from src.dao.tax_rate_dao import TaxRateDao
from src.dao.invoice_line_dao import InvoiceLineDao
# for adding or removing lines locally
from src.do.invoice import InvoiceLine
from src.database_manager import DatabaseManager

class InvoiceLinesModel(QAbstractTableModel):
    # Add a signal to notify when data changes that affects totals
    dataChanged = pyqtSignal(QModelIndex, QModelIndex, list)
    totalsChanged = pyqtSignal()

    def __init__(self, invoice_id=None, parent=None):
        super().__init__(parent)
        # Initialize all required DAOs
        self.initialize_daos()

        self.invoice_id = invoice_id
        self.invoice_lines = []
        self.headers = ["Item", "Account", "Description", "Quantity", "Unit Price", "Tax", "Subtotal", "Tax Amount", "Line Amount"]
        self.editable_columns = [0, 1, 2, 3, 4, 5]  # Item, Account, Description, Quantity, Unit Price, Tax
        self.changes = {}  # Track changes to save later
        self.new_lines = []  # Track new lines to be added
        self.deleted_line_ids = []  # Track lines to be deleted

        if invoice_id:
            self.load_data()

    def initialize_daos(self):
        """Initialize all DAOs with the same session"""
        # Get a shared database manager instance
        self.db_manager = DatabaseManager()

        self.invoice_dao = InvoiceDao()
        self.item_dao = ItemDao()
        self.account_dao = AccountDao()
        self.tax_rate_dao = TaxRateDao()
        self.invoice_line_dao = InvoiceLineDao()

    def load_data(self):
        """Load invoice lines for the specified invoice"""
        invoice = self.invoice_dao.get_invoice_with_lines(self.invoice_id)
        if invoice and hasattr(invoice, 'invoice_lines'):
            # Make sure relationships are loaded
            self.invoice_lines = []
            for line in invoice.invoice_lines:
                # Ensure item, account, and tax_rate are loaded
                if hasattr(line, 'item_id') and line.item_id:
                    line.item = self.item_dao.get_item_by_id(line.item_id)
                if hasattr(line, 'account_id') and line.account_id:
                    line.account = self.account_dao.get_account_by_id(line.account_id)
                if hasattr(line, 'tax_rate_id') and line.tax_rate_id:
                    line.tax_rate = self.tax_rate_dao.get_tax_rate(line.tax_rate_id)
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
                    invoice_line.item = self.item_dao.get_item_by_id(invoice_line.item_id)

                return invoice_line.item.name if hasattr(invoice_line, 'item') and invoice_line.item else ""

            elif column == 1:  # Account
                # If account_id is None, return empty string to represent blank option
                if not hasattr(invoice_line, 'account_id') or invoice_line.account_id is None:
                    return ""

                # If account is not loaded, try to load it
                if not hasattr(invoice_line, 'account') or invoice_line.account is None:
                    invoice_line.account = self.account_dao.get_account_by_id(invoice_line.account_id)

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
                        invoice_line.tax_rate = self.tax_rate_dao.get_tax_rate(invoice_line.tax_rate_id)

                tax_rate = invoice_line.tax_rate if hasattr(invoice_line, 'tax_rate') and invoice_line.tax_rate else None
                if tax_rate:
                    return f"{tax_rate.name}-{tax_rate.rate:.2f}%"
                return ""
            elif column == 6:  # Subtotal
                # Calculate subtotal as quantity * unit_price
                quantity = invoice_line.quantity if hasattr(invoice_line, 'quantity') and invoice_line.quantity is not None else 0
                unit_price = invoice_line.unit_price if hasattr(invoice_line, 'unit_price') and invoice_line.unit_price is not None else 0
                subtotal = quantity * unit_price
                return f"${subtotal:.2f}"
            elif column == 7:  # Tax Amount
                tax_amount = invoice_line.tax_amount if hasattr(invoice_line, 'tax_amount') and invoice_line.tax_amount is not None else 0
                return f"${tax_amount:.2f}"
            elif column == 8:  # Line Amount
                # Calculate line amount as subtotal + tax_amount
                quantity = invoice_line.quantity if hasattr(invoice_line, 'quantity') and invoice_line.quantity is not None else 0
                unit_price = invoice_line.unit_price if hasattr(invoice_line, 'unit_price') and invoice_line.unit_price is not None else 0
                subtotal = quantity * unit_price
                tax_amount = invoice_line.tax_amount if hasattr(invoice_line, 'tax_amount') and invoice_line.tax_amount is not None else 0
                line_amount = subtotal + tax_amount
                return f"${line_amount:.2f}"

        elif role == Qt.EditRole:
            # For edit role, return the raw value without formatting
            column = index.column()

            if column == 0:  # Item
                return invoice_line.item_id
            elif column == 1:  # Account
                return invoice_line.account_id
            elif column == 2:  # Description
                return invoice_line.description
            elif column == 3:  # Quantity
                return invoice_line.quantity
            elif column == 4:  # Unit Price
                return invoice_line.unit_price
            elif column == 5:  # Tax Rate
                return invoice_line.tax_rate_id
            # We don't need to handle columns 6, 7, 8 for EditRole as they're not editable

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
                    invoice_line.item = None
                    # invoice_line.item = self.item_dao.get_item_by_id(value)

                # Validate: either item or account must be specified
                if (invoice_line.item_id is None) == (invoice_line.account_id is None):
                    # Revert to original value
                    # invoice_line.item_id = original_item_id
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
                    invoice_line.account = None
                    # invoice_line.account = self.account_dao.get_account_by_id(value)

                # Validate: either item or account must be specified
                if (invoice_line.item_id is None) == (invoice_line.account_id is None):
                    # Revert to original value
                    # invoice_line.account_id = original_account_id
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
                tax_rate = self.tax_rate_dao.get_tax_rate(value) if value else None
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
            # self.dataChanged.emit(self.index(row, 0), self.index(row, self.columnCount() - 1))

            # After all changes, emit the dataChanged signal
            self.dataChanged.emit(index, index, [role])

            # If the change affects totals (quantity, unit_price, tax_amount), emit totalsChanged
            if col in [3, 4, 6]:  # Quantity, Unit Price, Tax Amount
                self.totalsChanged.emit()

            return True

        except (ValueError, TypeError) as e:
            print(f"Error setting data: {e}")
            return False

    def discard_changes(self):
        """Discard all unsaved changes and reset tracking variables"""
        # Clear all tracking lists
        self.new_lines = []
        self.changes = {}
        self.deleted_line_ids = []

        # Instead of removing the session, get a fresh session
        # First, get the current session
        session = self.db_manager.Session()

        # Rollback any uncommitted changes
        session.rollback()

        # Don't close or remove the session yet, as we need it for load_data

        # Reload data from database to reflect original state
        self.load_data()

        # # Now it's safe to clean up the session
        # session.close()
        # self.db_manager.remove_session()

        # Emit signal that totals have changed to update UI
        self.totalsChanged.emit()

    def has_unsaved_changes(self):
        """Check if there are any unsaved changes"""
        return len(self.changes) > 0 or len(self.new_lines) > 0 or len(self.deleted_line_ids) > 0

    def save_all_changes(self):
        """Save all changes to the database"""
        try:
            # Validate all lines before saving
            validation_errors = []

            # Check existing lines
            for line in self.invoice_lines:
                # Skip lines marked for deletion
                if line.id in self.deleted_line_ids:
                    continue

                # Validate: either item or account must be specified
                if (not hasattr(line, 'item_id') or line.item_id is None) and \
                   (not hasattr(line, 'account_id') or line.account_id is None):
                    validation_errors.append(f"Line '{line.description}': Either Item or Account must be specified")

                # Validate quantity
                if not hasattr(line, 'quantity') or line.quantity is None or line.quantity <= 0:
                    validation_errors.append(f"Line '{line.description}': Quantity must be greater than zero")

                # Validate unit price
                if not hasattr(line, 'unit_price') or line.unit_price is None or line.unit_price <= 0:
                    validation_errors.append(f"Line '{line.description}': Unit Price must be greater than zero")

                # Validate tax rate
                if not hasattr(line, 'tax_rate_id') or line.tax_rate_id is None:
                    validation_errors.append(f"Line '{line.description}': Tax Rate must be specified")

            # If there are validation errors, raise an exception
            if validation_errors:
                error_message = "Cannot save invoice due to the following errors:\n" + "\n".join(validation_errors)
                raise ValueError(error_message)

            # First, add all new lines
            for new_line in self.new_lines:
                # Convert the line object to a dictionary for the DAO
                line_data = {
                    'invoice_id': self.invoice_id,
                    'description': new_line.description,
                    'quantity': new_line.quantity,
                    'unit_price': new_line.unit_price,
                    'tax_amount': new_line.tax_amount,
                    'subtotal': new_line.quantity * new_line.unit_price,
                    'line_amount': (new_line.quantity * new_line.unit_price) + new_line.tax_amount,
                    'item_id': new_line.item_id,
                    'account_id': new_line.account_id,
                    'tax_rate_id': new_line.tax_rate_id
                }

                # Add to database using the specialized DAO
                self.invoice_line_dao.add_invoice_line(line_data)

            # Next, apply all changes to existing lines
            for line_id, changes in self.changes.items():
                # Skip changes for new lines (they were already added above)
                if line_id < 0:
                    continue

                # Update the line in the database using the specialized DAO
                self.invoice_line_dao.update_invoice_line(line_id, changes)

            # Finally, delete all lines marked for deletion
            for line_id in self.deleted_line_ids:
                self.invoice_line_dao.delete_invoice_line(line_id)

            # Recalculate invoice totals
            self.invoice_dao.recalculate_invoice_totals(self.invoice_id)

            # Clear all tracking lists
            self.new_lines = []
            self.changes = {}
            self.deleted_line_ids = []

            # Reload data from database to reflect all changes
            self.load_data()

            return True
        except Exception as e:
            print(f"Error saving changes: {str(e)}")
            return False

    # adding or removing lines locally
    def add_line_locally(self):
        """Add a new line to the model without saving to database"""
        # Create a temporary negative ID to identify new lines
        temp_id = -1 * (len(self.new_lines) + 1)

        # Get the default tax rate (assuming ID 1 is the default)
        default_tax_rate_id = 2
        tax_rates = self.get_available_tax_rates()
        if tax_rates and len(tax_rates) > 0:
            default_tax_rate_id = tax_rates[0].id

        # Create a new line object with default values
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
            tax_rate_id=default_tax_rate_id
        )

        # Add to our tracking list
        self.new_lines.append(new_line)

        # Add to the displayed lines
        self.beginInsertRows(QModelIndex(), len(self.invoice_lines), len(self.invoice_lines))
        self.invoice_lines.append(new_line)
        self.endInsertRows()

        # Emit signal that totals have changed
        self.totalsChanged.emit()

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

            # Emit signal that totals have changed
            self.totalsChanged.emit()

            return True
        return False

    # for dropdowns
    def get_available_items(self):
        """Get all available items for dropdown"""
        blank_item = type('BlankItem', (), {'id': None, 'name': ''})()
        items = self.item_dao.get_all_items()
        return [blank_item] + items

    def get_available_accounts(self):
        """Get all available accounts for dropdown"""
        blank_account = type('BlankAccount', (), {'id': None, 'name': ''})()
        accounts = self.account_dao.get_all_accounts()
        return [blank_account] + accounts

    def get_available_tax_rates(self):
        """Get all available tax rates for dropdown"""
        return self.tax_rate_dao.get_all_tax_rates()