from decimal import Decimal
import pandas as pd
from typing import List, Dict, Optional
from src.dao.data_access_object import DataAccessObject
from src.do.invoice import Invoice


class InvoiceDao(DataAccessObject):
    def __init__(self, is_testing: bool = False):
        super().__init__(table_name='invoices', is_testing=is_testing)

    def get_invoices_dataframe(self, conditions=None):
        query = f"""
        SELECT
            *
        FROM invoices
        """

        placeholders = self.extract_values_from_conditions(conditions) if conditions else None
        invoices_result = self.execute_select_query(query_str=query, placeholders=placeholders)

        invoices_df = pd.DataFrame(invoices_result.fetchall())
        if not invoices_df.empty:
            invoices_df.drop(['created_at'], axis='columns', inplace=True)
            new_columns = [column.replace('_', ' ').title() for column in invoices_df.columns]
            invoices_df.columns = new_columns

        return invoices_df

    @staticmethod
    def convert_to_decimal(value: float = 0, quantizer: str = '.00') -> Decimal:
        return Decimal(value).quantize(Decimal(quantizer))

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

    def get_invoices(self, conditions: Optional[Dict] = None,
                     columns: List[str] = ['id', 'invoice_number', 'date']) -> List[Invoice]:
        invoices_result = self.select(columns=columns, conditions=conditions)
        return [Invoice(**row) for row in invoices_result.fetchall()]
