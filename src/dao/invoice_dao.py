from typing import List, Dict, Optional
from decimal import Decimal

import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.do.invoice import Invoice
from src.database_manager import DatabaseManager
from src.logger import Logger

class InvoiceDao:
    def __init__(self, table_name=''):
        self.table_name = table_name
        self.db_manager = DatabaseManager()
        self.logger = Logger()

    def _convert_to_decimal(value: float = 0, quantizer: str = '.00') -> Decimal:
        return Decimal(value).quantize(Decimal(quantizer))


    def extract_filters(self, query, conditions):
        if not conditions:
            return query, {}

        where_clauses = []
        filters = {}

        for condition in conditions:
            column = condition.get('column')
            operator = condition.get('operator', '=')
            value = condition.get('value')
            connector = condition.get('connector', 'AND')

            if column and value is not None:
                param_name = f"{column.replace('.', '_')}_{len(filters)}"
                where_clauses.append(
                    f"{connector} {column} {operator} :{param_name}"
                )
                filters[param_name] = value

        if where_clauses:
            # Remove the connector in first clause
            where_clauses[0] = where_clauses[0].rsplit(' ', 1)[1]
            where_clause = " WHERE " + " ".join(where_clauses)
            query += where_clause

        return query, filters

    def execute_query(self, query_str, filters):
        """
        Execute the query_str
        :param query_str: The final query string with filters
        :param filters: A dictionary contains the values for the filters in the query string
        :return: Result of the query execution
        """

        with self.db_manager.Session() as session:
            try:
                session = self.db_manager.Session()
                result = session.execute(text(query_str), filters)
                session.commit()
                return result
            except SQLAlchemyError as e:
                session.rollback()
                return None

    def get_invoices_dataframe(self, conditions=None):
        query = f"""
        SELECT
            *
        FROM invoices
        """

        query_str, filters = self.extract_filters(query, conditions)
        print(query_str)
        print(filters)
        invoices_result = self.execute_query(query_str=query_str, filters=filters)

        invoices_df = pd.DataFrame(invoices_result.fetchall())
        if not invoices_df.empty:
            invoices_df.drop(['created_at'], axis='columns', inplace=True)
            new_columns = [column.replace('_', ' ').title() for column in invoices_df.columns]
            invoices_df.columns = new_columns

        return invoices_df


    def create_invoice(self, invoice: Invoice) -> Optional[int]:
        invoice_values = {
            'invoice_number': invoice.invoice_number,
            'date': invoice.date,
            'customer_id': invoice.customer_id,
            'due_date': invoice.due_date,
            'subtotal': invoice.subtotal,
            'tax_amount': invoice.tax_amount,
            'total_amount': invoice.total_amount,
            'description': invoice.description,
            'status': invoice.status
        }
        return self.insert(values=invoice_values)

