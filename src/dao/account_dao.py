from src.dao.data_access_object import DataAccessObject
from src.do.account import Account


class AccountDao(DataAccessObject):
    def __init__(self, is_testing=False):
        super().__init__(table_name='accounts', is_testing=is_testing)

    def get_all_accounts(self):
        """Get all available accounts"""
        try:
            return self.session.query(Account).all()
        except Exception as e:
            self.logger.error(f"Error getting all accounts: {str(e)}")
            return []

    def get_account_by_id(self, account_id):
        """Get an account by ID"""
        try:
            return self.session.query(Account).filter(Account.id == account_id).first()
        except Exception as e:
            self.logger.error(f"Error getting account by ID: {str(e)}")
            return None