from src.dao.data_access_object import DataAccessObject
from src.do.customer import Customer

class CustomerDao(DataAccessObject):
    def __init__(self, is_testing=False):
        super().__init__(table_name='customers', is_testing=is_testing)

    def get_all_customers(self, filters=None):
        """Get all customers with related data"""
        try:
            query = self.session.query(Customer)

            # Apply customer filters
            if filters:
                for filter_condition in filters:
                    query = query.filter(filter_condition)
            return query.all()
        except Exception as e:
            self.logger.error(f"Error getting all customers: {str(e)}")
            return []

    def get_customer_by_id(self, customer_id):
        """Get an customer by ID with related data"""
        try:
            return self.session.query(Customer).filter(Customer.id == customer_id).first()
        except Exception as e:
            self.logger.error(f"Error getting customer by ID: {str(e)}")
            return None

    def create_customer(self, customer_data):
        """Create a new customer"""
        try:
            customer = Customer(**customer_data)
            self.session.add(customer)
            self.session.commit()
            return customer
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error creating customer: {str(e)}")
            return None

    def update_customer(self, customer_id, customer_data):
        """Update an existing customer"""
        try:
            customer = self.get_customer_by_id(customer_id)
            if not customer:
                return None

            for key, value in customer_data.items():
                setattr(customer, key, value)

            self.session.commit()
            return customer
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error updating customer: {str(e)}")
            return None

    def delete_customer(self, customer_id):
        """Delete an customer"""
        try:
            customer = self.get_customer_by_id(customer_id)
            if not customer:
                return False

            self.session.delete(customer)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error deleting customer: {str(e)}")
            return False