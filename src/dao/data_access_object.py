from src.database_manager import DatabaseManager
from src.logger import Logger


class DataAccessObject:
    def __init__(self, table_name='', is_testing=False):
        """
        Initialize the DAO with a database session

        Args:
            table_name: The name of the table this DAO manages
            is_testing: Whether to use the testing database
        """
        self.db_manager = DatabaseManager(is_testing)
        self.table_name = table_name

        # Get the current session from the session factory
        self.session = self.db_manager.Session()

        self.logger = Logger()
