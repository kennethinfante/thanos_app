from src.dao.data_access_object import DataAccessObject
from src.do.tax_rate import TaxRate


class TaxRateDao(DataAccessObject):
    def __init__(self, is_testing=False):
        super().__init__(table_name='tax_rates', is_testing=is_testing)

    def get_all_tax_rates(self):
        """Get all available tax rates"""
        try:
            return self.session.query(TaxRate).all()
        except Exception as e:
            self.logger.error(f"Error getting all tax rates: {str(e)}")
            return []

    def get_tax_rate(self, tax_rate_id):
        """Get a specific tax rate by ID"""
        try:
            return self.session.query(TaxRate).filter(TaxRate.id == tax_rate_id).first()
        except Exception as e:
            self.logger.error(f"Error getting tax rate by ID: {str(e)}")
            return None