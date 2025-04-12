from typing import List, Dict, Optional

from decimal import Decimal
import pandas as pd

from src.dao.data_access_object import DataAccessObject
from src.do.invoice import Invoice

class InvoiceDao(DataAccessObject):
    def __init__(self, is_testing: bool = False):
        super().__init__(table_name='invoices', is_testing=is_testing)

    def _convert_to_decimal(value: float = 0, quantizer: str = '.00') -> Decimal:
        return Decimal(value).quantize(Decimal(quantizer))

    def get_invoices_dataframe(self, conditions=None):
        query = f"""
        SELECT
            *
        FROM invoices
        """

        filter_clauses, placeholders = self.build_filter_clauses_and_placeholders(conditions)
        query_str = self.build_query_string(query, filter_clauses)

        print(query_str, filter_clauses, placeholders)
        invoices_result = self.execute_select_query(query_str=query_str, placeholders=placeholders)

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

