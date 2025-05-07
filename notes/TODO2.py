from typing import Dict, List, Any, Optional
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from src.database_manager import DatabaseManager
from src.logger import Logger

class DataAccessObject:
    def __init__(self, table_name: str = '', is_testing: bool = False):
        self.table_name = table_name
        self.logger = Logger()
        self.db_manager = DatabaseManager(is_testing)

    def debug_query(self, result: Any = None, error: Optional[str] = None) -> bool:
        """Log query errors."""
        if error:
            self.logger.debug(f"Query errors: {error}")
            return False
        return True

    def execute_query(self, query_str: str, place_holders: Dict[str, Any]) -> Optional[Any]:
        """Execute a query with commit."""
        try:
            with self.db_manager.Session() as session:
                result = session.execute(text(query_str), place_holders)
                session.commit()
                return result
        except SQLAlchemyError as e:
            session.rollback()
            self.debug_query(error=str(e))
            return None

    def execute_select_query(self, query_str: str, placeholders: Optional[Dict[str, Any]] = None) -> Optional[Any]:
        """Execute a read-only query."""
        try:
            with self.db_manager.Session() as session:
                return session.execute(text(query_str), placeholders or {})
        except SQLAlchemyError as e:
            self.debug_query(error=str(e))
            return None

    def execute_edit_query(self, query_str: str, place_holders: Optional[Dict[str, Any]] = None) -> Optional[int]:
        """Execute a query that modifies data."""
        try:
            with self.db_manager.Session() as session:
                result = session.execute(text(query_str), place_holders or {})
                last_id = result.lastrowid
                session.commit()
                return last_id
        except SQLAlchemyError as e:
            session.rollback()
            self.debug_query(error=str(e))
            return None

    def select(self, columns: Optional[List[str]] = None, conditions: Optional[List[Dict[str, Any]]] = None, table_name: str = '') -> Optional[Any]:
        """Get columns with conditions and values."""
        table = table_name or self.table_name
        cols = ','.join(columns) if columns else '*'
        cond = self.build_conditions(conditions) if conditions else ''
        query_str = f"SELECT {cols} FROM {table} {cond}"
        placeholders = self.extract_values_from_conditions(conditions) if conditions else None
        return self.execute_select_query(query_str, placeholders)

    def insert(self, values: Dict[str, Any], table_name: str = '') -> Optional[int]:
        """Insert values into the table."""
        table = table_name or self.table_name
        query_str = self.build_insert_query(values.keys(), table)
        return self.execute_edit_query(query_str=query_str, place_holders=values)

    def extract_values_from_conditions(self, conditions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract values from conditions for placeholders."""
        return {
            condition.get('parameter') or condition['column'].replace('.', '_'): condition['value']
            for condition in conditions
        }

    @staticmethod
    def build_conditions(conditions: List[Dict[str, Any]]) -> str:
        """Build the WHERE clause for SQL queries."""
        return ' WHERE ' + ' AND '.join(
            f"{cond['column']} {cond['operator']} :{cond.get('parameter') or cond['column'].replace('.', '_')}"
            for cond in conditions
        )

    @staticmethod
    def build_insert_query(columns: List[str], table_name: str) -> str:
        """Build an INSERT query."""
        cols = ', '.join(columns)
        placeholders = ', '.join(f':{col}' for col in columns)
        return f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"

    # You might want to implement build_bulk_insert_query here if needed