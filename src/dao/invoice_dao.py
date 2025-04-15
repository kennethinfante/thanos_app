from src.dao.data_access_object import DataAccessObject
from src.do.invoice import Invoice

class InvoiceDao(DataAccessObject):
    def __init__(self, is_testing=False):
        super().__init__(table_name='invoices', is_testing=is_testing)

    def get_all_invoices(self, filters=None):
        """Get all invoices with related data"""
        try:
            query = self.session.query(Invoice)
            query = query.join(Invoice.customer)

            # Apply invoice filters
            if filters:
                for filter_condition in filters:
                    query = query.filter(filter_condition)
            return query.all()
        except Exception as e:
            self.logger.error(f"Error getting all invoices: {str(e)}")
            return []

    def get_invoice_by_id(self, invoice_id):
        """Get an invoice by ID with related data"""
        try:
            return self.session.query(Invoice).filter(Invoice.id == invoice_id).first()
        except Exception as e:
            self.logger.error(f"Error getting invoice by ID: {str(e)}")
            return None

    # Add this method to the InvoiceDao class
    def get_invoice_with_lines(self, invoice_id):
        """Get an invoice with its line items"""
        try:
            invoice = self.session.query(Invoice).filter(Invoice.id == invoice_id).first()
            # This will load the invoice lines due to the relationship
            return invoice
        except Exception as e:
            self.logger.error(f"Error getting invoice with lines: {str(e)}")
            return None

    def get_invoices_by_customer(self, customer_id):
        """Get all invoices for a specific customer"""
        try:
            return self.session.query(Invoice).filter(Invoice.customer_id == customer_id).all()
        except Exception as e:
            self.logger.error(f"Error getting invoices by customer: {str(e)}")
            return []

    def create_invoice(self, invoice_data):
        """Create a new invoice"""
        try:
            invoice = Invoice(**invoice_data)
            self.session.add(invoice)
            self.session.commit()
            return invoice
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error creating invoice: {str(e)}")
            return None

    def update_invoice(self, invoice_id, invoice_data):
        """Update an existing invoice"""
        try:
            invoice = self.get_invoice_by_id(invoice_id)
            if not invoice:
                return None

            for key, value in invoice_data.items():
                setattr(invoice, key, value)

            self.session.commit()
            return invoice
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error updating invoice: {str(e)}")
            return None

    def delete_invoice(self, invoice_id):
        """Delete an invoice"""
        try:
            invoice = self.get_invoice_by_id(invoice_id)
            if not invoice:
                return False

            self.session.delete(invoice)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error deleting invoice: {str(e)}")
            return False

    # for editing invoice lines
    def get_invoice_with_lines(self, invoice_id):
        """Get an invoice with its line items"""

        try:
            invoice = self.session.query(Invoice).filter(Invoice.id == invoice_id).first()
            # This will load the invoice lines due to the relationship
            return invoice
        except Exception as e:
            print(f"Error getting invoice with lines: {e}")
            return None

    def add_invoice_line(self, invoice_line):
        """Add a new invoice line"""

        try:
            self.session.add(invoice_line)
            self.session.commit()

            # Calculate subtotal and line amount
            invoice_line.subtotal = invoice_line.quantity * invoice_line.unit_price
            invoice_line.line_amount = invoice_line.subtotal + invoice_line.tax_amount

            session.commit()
            return invoice_line
        except Exception as e:
            session.rollback()
            print(f"Error adding invoice line: {e}")
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

            self.session.commit()
            return invoice_line
        except Exception as e:
            self.session.rollback()
            print(f"Error updating invoice line: {e}")
            return None

    def delete_invoice_line(self, line_id):
        """Delete an invoice line"""

        try:
            # Get the invoice line
            invoice_line = self.session.query(InvoiceLine).filter(InvoiceLine.id == line_id).first()

            if not invoice_line:
                return False

            # Delete the invoice line
            self.session.delete(invoice_line)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print(f"Error deleting invoice line: {e}")
            return False

    def recalculate_invoice_totals(self, invoice_id):
        """Recalculate invoice totals based on line items"""

        try:
            # Get the invoice with its lines
            invoice = self.session.query(Invoice).filter(Invoice.id == invoice_id).first()

            if not invoice:
                return False

            # Calculate totals
            subtotal = sum(line.subtotal for line in invoice.invoice_lines)
            tax_amount = sum(line.tax_amount for line in invoice.invoice_lines)
            total_amount = subtotal + tax_amount

            # Update the invoice
            invoice.subtotal = subtotal
            invoice.tax_amount = tax_amount
            invoice.total_amount = total_amount

            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print(f"Error recalculating invoice totals: {e}")
            return False
