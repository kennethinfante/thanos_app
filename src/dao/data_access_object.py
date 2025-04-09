from src.logger import Logger
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from src.database_manager import DatabaseManager

class DataAccessObject(object):
    def __init__(self, table_name='', is_testing=False):
        self.table_name = table_name
        self.logger = Logger()
        self.db_manager = DatabaseManager(is_testing)

    def debug_query(self, result=None, error=None):
        """
        This function logs query errors
        :param result: Query result
        :param error: Error message if any
        :return: True if no errors, False instead
        """
        if error:
            self.logger.debug(f"Query errors: {error}")
            return False
        return True

    def execute_query(self, query_str, place_holders):
        """
        Execute the query_str
        :param query_str: The final query string with placeholders
        :param place_holders: A dictionary contains the values for the placeholders in the query string
        :return: Result of the query execution
        """
        try:
            session = self.db_manager.Session()
            result = session.execute(text(query_str), place_holders)
            session.commit()
            return result
        except SQLAlchemyError as e:
            session.rollback()
            self.debug_query(error=str(e))
            return None
        finally:
            session.close()

    def execute_select_query(self, query_str, placeholders=None):
        """
        Execute a query that will fetch (Read only) data from the database
        :param query_str: The final query string with placeholders
        :param placeholders: A dictionary contains the values for the placeholders in the query string
        :return: result if it's successful None instead
        """
        try:
            session = self.db_manager.Session()
            result = session.execute(text(query_str), placeholders or {})
            return result
        except SQLAlchemyError as e:
            self.debug_query(error=str(e))
            return None
        finally:
            session.close()

    def execute_edit_query(self, query_str, place_holders=None):
        """
        Execute a query that will modify (Write) data in the database
        :param query_str: The final query string with placeholders
        :param place_holders: A dictionary contains the values for the placeholders in the query string
        :return: Last inserted ID in case of success None instead
        """
        try:
            session = self.db_manager.Session()
            result = session.execute(text(query_str), place_holders or {})
            last_id = result.lastrowid
            session.commit()
            return last_id
        except SQLAlchemyError as e:
            session.rollback()
            self.debug_query(error=str(e))
            return None
        finally:
            session.close()

    def select(self, columns=None, conditions=None, table_name=''):
        """
        Get the columns with conditions and values
        :param columns: The columns we want to retrieve from the table, if not presented use '*' instead
        :param conditions: Dictionary contains the required conditions on the query
        :return: Query result after execution
        """
        query_str = f"""SELECT {",".join(columns) if columns else '*'} FROM {self.table_name if table_name== '' else table_name} {self.build_conditions(conditions) if conditions else ''}"""
        placeholders = self.extract_values_from_conditions(conditions) if conditions else None
        return self.execute_select_query(query_str, placeholders)

    def insert(self, values, table_name=''):
        """
        Insert the 'values', the values keys represents placeholders and column names
        :param values: Dictionary contains the columns names which act as placeholders and its values
        :return: Query result after executing
        """
        query_str = self.build_insert_query(values.keys(), table_name) if isinstance(values, dict) else self.build_bulk_insert_query(values, table_name)
        return self.execute_edit_query(query_str=query_str, place_holders=values)

    def extract_values_from_conditions(self, conditions):
        placeholder = dict()
        for condition in conditions:
            placeholder_key = condition['column'].replace('.', '_') if not 'parameter' in condition else condition['parameter']
            placeholder[placeholder_key] = condition['value']
        return placeholder


    # The bind_values method is no longer needed as SQLAlchemy handles parameter binding differently
    # Other methods like build_conditions, build_insert_query, etc. can remain largely the same
    # as they're just building SQL strings