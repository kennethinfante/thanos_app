from src.database_manager import DatabaseManager
from src.logger import Logger

class DataAccessObject:
    def __init__(self, table_name='', is_testing=False):
        self.table_name = table_name
        self.logger = Logger()
        self.db_manager = DatabaseManager(is_testing)
        self.session = self.db_manager.Session()

    def get_all(self):
        """Get all records from the table"""
        try:
            table = self.db_manager.metadata.tables[self.table_name]
            result = self.session.query(table).all()
            return result
        except Exception as e:
            self.logger.error(f"Error getting all records from {self.table_name}: {str(e)}")
            return []

    def get_by_id(self, id):
        """Get a record by ID"""
        try:
            table = self.db_manager.metadata.tables[self.table_name]
            result = self.session.query(table).filter_by(id=id).first()
            return result
        except Exception as e:
            self.logger.error(f"Error getting record by ID from {self.table_name}: {str(e)}")
            return None

    def close(self):
        """Close the session"""
        self.session.close()