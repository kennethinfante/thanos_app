from typing import List, Dict, Optional

from decimal import Decimal
import pandas as pd

from src.dao.data_access_object import DataAccessObject
from src.do.item import Item

class ItemDao(DataAccessObject):
    def __init__(self, is_testing: bool = False):
        super().__init__(table_name='items', is_testing=is_testing)

    def _convert_to_decimal(value: float = 0, quantizer: str = '.00') -> Decimal:
        return Decimal(value).quantize(Decimal(quantizer))

    def get_items_dataframe(self, conditions=None):
        query = f"""
        SELECT
            *
        FROM items
        """

        filter_clauses, placeholders = self.build_filter_clauses_and_placeholders(conditions)
        query_str = self.build_query_string(query, filter_clauses)

        print(query_str, filter_clauses, placeholders)
        items_result = self.execute_select_query(query_str=query_str, placeholders=placeholders)

        items_df = pd.DataFrame(items_result.fetchall())
        if not items_df.empty:
            items_df.drop(['created_at'], axis='columns', inplace=True)
            new_columns = [column.replace('_', ' ').title() for column in items_df.columns]
            items_df.columns = new_columns

        return items_df

