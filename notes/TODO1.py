### DAO
from typing import Dict, List, Any, Optional
from src.database_manager import DatabaseManager
from src.logger import Logger

class DataAccessObject:
    def __init__(self, table_name: str = '', is_testing: bool = False):
        self.table_name = table_name
        self.logger = Logger()
        self.db_manager = DatabaseManager(is_testing)

    def execute_select_query(self, query_str: str, placeholders: Optional[Dict[str, Any]] = None):
        try:
            return self.db_manager.execute_query(query_str, placeholders)
        except Exception as e:
            self.logger.error(f"Error executing select query: {e}")
            return None

    def select(self, columns: List[str], conditions: Optional[Dict[str, Any]] = None) -> Optional[Any]:
        query = f"SELECT {', '.join(columns)} FROM {self.table_name}"
        if conditions:
            query += f" WHERE {self.build_conditions(conditions)}"
        return self.execute_select_query(query, self.extract_values_from_conditions(conditions))

    def insert(self, values: Dict[str, Any]) -> Optional[int]:
        columns = ', '.join(values.keys())
        placeholders = ', '.join([f':{key}' for key in values.keys()])
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        try:
            result = self.db_manager.execute_query(query, values)
            return result.lastInsertId() if result else None
        except Exception as e:
            self.logger.error(f"Error inserting data: {e}")
            return None

    @staticmethod
    def build_conditions(conditions: Dict[str, Any]) -> str:
        return ' AND '.join([f"{cond['column']} {cond['operator']} :{cond['column']}" for cond in conditions])

    @staticmethod
    def extract_values_from_conditions(conditions: Dict[str, Any]) -> Dict[str, Any]:
        return {cond['column']: cond['value'] for cond in conditions}

