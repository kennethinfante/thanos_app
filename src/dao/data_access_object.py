from collections import ChainMap
from PyQt5.QtSql import QSqlQuery
from src.database_manager import DatabaseManager
from src.logger import Logger
import copy


class DataAccessObject(object):
    def __init__(self, table_name='', is_testing=False):
        self.data_base = DatabaseManager(is_testing=is_testing)
        self.table_name = table_name
        self.logger = Logger()

    def debug_query(self, query: QSqlQuery):
        """
        This function takes QSqlQuery object and pass it to the logger class
        :param query:
        :return: True if no errors, False instead
        """
        self.logger.debug("Query errors: " + query.lastError().text())
        return True if not query.lastError().text() else False

    def build_insert_query(self, cols, table_name=''):
        """
        Takes a list of strings that represents the columns in the INSERT query, and place it in VALUES with
        :param table_name: An optional string indicates the table name to be used in the insert query, it can be
        overriden by the class's table name
        :param cols: List of strings represents the columns we want to insert
        :return: A string containing the INSERT statement without real values (only placeholders),
        placeholders are added in bind_values function
        """
        cols_values = "VALUES ("
        cols_names = ""
        query = f"INSERT INTO {self.table_name if table_name == '' else table_name}("
        for col_name in cols:
            cols_names += col_name + ","
            cols_values += f":{col_name},"
        query += f"{cols_names[:-1]}) {cols_values[:-1]})"
        return query

    def build_bulk_insert_query(self, values, table_name=''):
        cols = copy.deepcopy(values[0])
        self.assign_placeholders(values)
        query = f"INSERT INTO {self.table_name if table_name == '' else table_name} " \
                f"({','.join(col_name for col_name in cols.keys())}) VALUES " \
                f"{','.join([self.build_values_rows(row) for row in values])}"
        return query

    def assign_placeholders(self, values):
        old_keys = copy.deepcopy(values[0])
        for i in range(len(values)):
            for j in old_keys:
                new_key = f'{j}_{i}'
                values[i][new_key] = values[i].pop(j)

    def build_values_rows(self, row):
        """
        Build a row to with placeholders to be inserted in bulk insertion
        :param row: A dictionary to be inserted
        :return: A string represents the row to be inserted (:col_1_index, :col_2_index, etc ...)
        """
        return f"({','.join([':'+col_name for col_name in row])})"

    def bind_values(self, query: QSqlQuery, values: dict):
        """
        Bind the values in the values to its corresponding placeholder from the query
        :param query: QSqlQuery with placeholders
        :param values: A dictionary contains the values to placeholders in query object,
        the dictionary keys are the same as the placeholders names
        :return: None, as query is passed by reference
        """
        values = dict(ChainMap(*values)) if isinstance(values, list) else values
        [query.bindValue(f':{value}', values[value]) for value in values.keys()]

    def insert(self, values, table_name=''):
        """
        Insert the 'values', the values keys represents placeholders and column names
        :param values: Dictionary contains the columns names which act as placeholders and its values
        :return: QSqlQuery object after executing
        """
        query_str = self.build_insert_query(values.keys(), table_name) if isinstance(values, dict) else self.build_bulk_insert_query(values, table_name)
        return self.execute_edit_query(query_str=query_str, place_holders=values)

    def build_conditions(self, conditions):
        """
        This function builds conditions for the SELECT query, based on whether the required widget has something in it
        or not
        :return:
        """
        #Remove the logic operator from the first condition
        conditions[0]['logic'] = ''
        return ' WHERE ' + ' '.join([self.get_condition_string(condition) for condition in conditions]) if any(
            conditions) else ""

    def get_condition_string(self, condition):
        """
        Get a condition string out of a condition object
        :param condition: A condition object contains the required parameters for the condition
        :return: A condition string to be used in SQL query
        """
        return f"{condition['logic']} {condition['column']} {condition['operator']} :{condition['parameter'] if 'parameter' in condition else condition['column'].replace('.', '_')} {condition['options']}"

    def select(self, columns=None, conditions=None, table_name=''):
        """
        Get the columns with conditions and values
        :param columns: The columns we want to retrieve from the table, if not presented use '*' instead
        :param conditions: Dictionary contains the required conditions on the query
        :return: QSqlQuery object after execution
        """
        query_str = f"""SELECT {",".join(columns) if columns else '*'} FROM {self.table_name if table_name== '' else table_name} {self.build_conditions(conditions) if conditions else ''}"""
        placeholders = self.extract_values_from_conditions(conditions) if conditions else None
        return self.execute_select_query(query_str, placeholders)

    def execute_select_query(self, query_str, placeholders=None):
        """
        Execute a QSqlQuery object that will fetch (Read only) data from the database
        :param query_str: The final query string with placeholders
        :param placeholders: A dictionary contains the values for the palceholders in the query string
        :return: query (with data) if it's successful None instead
        """
        query = self.execute_query(query_str, place_holders=placeholders)
        return query if self.debug_query(query) else None

    def execute_edit_query(self, query_str, place_holders=None):
        """
        Execute a QSqlQuery object that will modify (Write) data in the database
        :param query_str: The final query string with placeholders
        :param place_holders: A dictionary contains the values for the palceholders in the query string
        :return: True in case of success False instead
        """
        query = self.execute_query(query_str, place_holders=place_holders)
        return query.lastInsertId() if self.debug_query(query) else None

    def execute_query(self, query_str, place_holders):
        """
        Execute the query_str
        :param query_str: The final query string with placeholders
        :param place_holders: A dictionary contains the values for the palceholders in the query string
        :return: A QSqlQuery object after execution
        """
        query = QSqlQuery()
        query.prepare(query_str)
        if place_holders:
            self.bind_values(query, place_holders)
        query.exec_()
        return query

    def update(self, values, conditions):
        placeholders = dict()
        query_str = self.build_update_string(values.keys()) + self.build_conditions(conditions)
        for value in values.keys():
            placeholders[value] = values[value]
        placeholders.update(self.extract_values_from_conditions(conditions))
        self.execute_edit_query(query_str, placeholders)

    def build_update_string(self, columns):
        new_cols = ""
        query = f"UPDATE {self.table_name} SET "
        for col_name in columns:
            new_cols += f"{col_name}=:{col_name},"
        query += new_cols[:-1]
        return query

    def delete(self, conditions):
        placeholders = self.extract_values_from_conditions(conditions)
        query_str = f'DELETE FROM {self.table_name} {self.build_conditions(conditions)}'
        return self.execute_edit_query(query_str, place_holders=placeholders)

    def extract_values_from_conditions(self, conditions):
        placeholder = dict()
        for condition in conditions:
            placeholder_key = condition['column'].replace('.', '_') if not 'parameter' in condition else condition['parameter']
            placeholder[placeholder_key] = condition['value']
        return placeholder

    def get_data_for_completer(self, column):
        """
        Get a list of strings contains the data for the column
        :param column:
        :return: QListString contains the data in 'column'
        """
        column_values_result = self.select(columns=[column,])
        column_values = []
        while column_values_result.next():
            column_values.append(str(column_values_result.value(column)))
        return column_values
