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

    def get_invoices_by_customer(self, customer_id):
        """Get all invoices for a specific customer"""
        try:
            return self.session.query(Invoice).filter(Invoice.customer_id == customer_id).all()
        except Exception as e:
            self.logger.error(f"Error getting invoices by customer: {str(e)}")
            return []

    def search_invoices(self, filters):
        """Search invoices based on filters"""
        try:
            query = self.session.query(Invoice)

            for filter_condition in filters:
                query = query.filter(filter_condition)

            return query.all()
        except Exception as e:
            self.logger.error(f"Error searching invoices: {str(e)}")
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