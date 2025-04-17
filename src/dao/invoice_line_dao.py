from src.dao.data_access_object import DataAccessObject
from src.do.invoice import InvoiceLine


class InvoiceLineDao(DataAccessObject):
    def __init__(self, is_testing=False):
        super().__init__(table_name='invoice_lines', is_testing=is_testing)

    def add_invoice_line(self, line_data):
        """Add a new invoice line"""
        try:
            # Create a new InvoiceLine object from the dictionary
            invoice_line = InvoiceLine()

            # Set attributes from the dictionary
            for key, value in line_data.items():
                # Skip setting the id field - let SQLAlchemy handle it
                if key != 'id':
                    setattr(invoice_line, key, value)

            # Calculate subtotal and line amount BEFORE adding to session
            invoice_line.subtotal = invoice_line.quantity * invoice_line.unit_price
            invoice_line.line_amount = invoice_line.subtotal + invoice_line.tax_amount

            # Add to session and commit once
            self.session.add(invoice_line)
            self.session.flush()
            self.session.commit()

            line_id = invoice_line.id

            # Clear the session to ensure we get a fresh object
            self.session.expunge_all()

            # Query for the newly created line with a fresh session
            new_line = self.session.query(InvoiceLine).get(line_id)
            return new_line

        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error adding invoice line: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
            return None

    def update_invoice_line(self, line_id, line_data):
        """Update an existing invoice line"""
        try:
            # Get the invoice line
            invoice_line = self.session.query(InvoiceLine).filter(InvoiceLine.id == line_id).first()

            if not invoice_line:
                return None

            # Update the invoice line with the provided data
            for key, value in line_data.items():
                setattr(invoice_line, key, value)

            # Ensure subtotal and line amount are calculated correctly
            invoice_line.subtotal = invoice_line.quantity * invoice_line.unit_price
            invoice_line.line_amount = invoice_line.subtotal + invoice_line.tax_amount

            # Flush changes to the database but don't commit yet
            self.session.flush()
            self.session.commit()

            return invoice_line
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error updating invoice line: {e}")
            return None

    def delete_invoice_line(self, line_id):
        """Delete an invoice line"""
        try:
            # Get the invoice line
            invoice_line = self.session.query(InvoiceLine).filter(InvoiceLine.id == line_id).first()

            if not invoice_line:
                return False

            # Calculate subtotal and line amount BEFORE adding to session
            invoice_line.subtotal = invoice_line.quantity * invoice_line.unit_price
            invoice_line.line_amount = invoice_line.subtotal + invoice_line.tax_amount

            # Delete the invoice line
            self.session.delete(invoice_line)
            self.session.flush()
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error deleting invoice line: {e}")
            return False