from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.logger import Logger
from src.database_manager import DatabaseManager

class DataAccessObject(object):
    def __init__(self, table_name='', is_testing=False):
        self.table_name = table_name
        self.logger = Logger()
        self.db_manager = DatabaseManager(is_testing)

    def build_query_string(self, query, filter_clauses=None):
        if filter_clauses:
            # Remove the connector in first clause
            filter_clauses[0] = filter_clauses[0].rsplit(' ', 1)[1]
            where_clause = " WHERE " + " ".join(filter_clauses)
            query += where_clause

        return query

    def build_filter_clauses_and_placeholders(self, conditions=None):
        filter_clauses = []
        placeholders = {}

        if not conditions:
            return filter_clauses, placeholders

        for condition in conditions:
            column = condition.get('column')
            operator = condition.get('operator', '=')
            value = condition.get('value')
            connector = condition.get('connector', 'AND')

            if column and value is not None:
                param_name = f"{column.replace('.', '_')}_{len(placeholders)}"
                filter_clauses.append(
                    f"{connector} {column} {operator} :{param_name}"
                )
                placeholders[param_name] = value

        return filter_clauses, placeholders

    def debug_query(self, error=None):
        if error:
            self.logger.debug(f"Query errors: {error}")
            return False
        return True

    def execute_select_query(self, query_str, placeholders=None):
        with self.db_manager.Session() as session:
            try:
                result = session.execute(text(query_str), placeholders or {})
                return result
            except SQLAlchemyError as e:
                self.debug_query(error=str(e))
                return None

    def execute_edit_query(self, query_str, placeholders=None):
        with self.db_manager.Session() as session:
            try:
                result = session.execute(text(query_str), placeholders or {})
                last_id = result.lastrowid
                session.commit()
                return last_id
            except SQLAlchemyError as e:
                session.rollback()
                self.debug_query(error=str(e))
                return None

    def execute_query(self, query_str, placeholders):
        with self.db_manager.Session() as session:
            try:
                session = self.db_manager.Session()
                result = session.execute(text(query_str), placeholders)
                session.commit()
                return result
            except SQLAlchemyError as e:
                session.rollback()
                return None