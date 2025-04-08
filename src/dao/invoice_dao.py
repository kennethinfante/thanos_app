import pandas as pd
from decimal import Decimal
from src.dao.data_access_object import DataAccessObject
from src.do.invoice import Invoice


class InvoiceDao(DataAccessObject):
    def __init__(self, is_testing=False):
        super(InvoiceDao, self).__init__(table_name='invoices', is_testing=is_testing)

    def create_invoice(self, invoice):
        invoice_values = {'serial_number': invoice.get_serial_number(),
                          'date': invoice.get_date(),
                          'employee_id': invoice.get_employee().id,
                          'customer_id': invoice.get_customer().id}
        invoice_id = self.insert(values=invoice_values)
        return self.set_invoice_products(invoice_id, invoice.get_products()) if invoice_id > 0 else None

    def get_invoices(self, conditions, columns=['id', 'serial_number', 'date']):
        invoices = []
        invoices_result = self.select(columns=columns, conditions=conditions)
        while invoices_result.next():
            invoices.append(Invoice(invoice_id=invoices_result.value('id'),
                                    serial_number=invoices_result.value('serial_number'),
                                    date=invoices_result.value('date')))
        return invoices

    def set_invoice_products(self, invoice_id, products):
        return invoice_id if self.insert([{'invoice_id': invoice_id, 'product_id': product} for product in products],
                                         table_name='invoices_products') else -1

    # def get_invoices_dataframe(self, conditions=None):
    #     query = f"""
    #     SELECT invoice.id AS invoice_id, invoice.serial_number AS serial_number, invoice.date AS invoice_date,
    #     invoice.accessories AS accessories, invoice.above_installation AS above_installation,
    #     invoices_products.quantity AS quantity, SUM(products.price*invoices_products.quantity) AS products_total
    #     FROM invoices AS invoice INNER JOIN invoices_products ON invoice.id=invoices_products.invoice_id
    #     INNER JOIN products ON invoices_products.product_id=products.id
    #     {self.build_conditions(conditions) if conditions else ''} GROUP BY(invoice_id)
    #     """
    #
    #     placeholders = self.extract_values_from_conditions(conditions) if conditions else None
    #     invoices_result = self.execute_select_query(query_str=query, placeholders=placeholders)
    #     invoices = []
    #     while invoices_result.next():
    #         invoice = Invoice(invoice_id=invoices_result.value('invoice_id'),
    #                           serial_number=invoices_result.value('serial_number'),
    #                           date=invoices_result.value('invoice_date'),
    #                           accessories=invoices_result.value('accessories'),
    #                           above_installation=invoices_result.value('above_installation')).serialize_invoice(exclude=['products', 'employees_shares'])
    #         invoice["Total"] = self.convert_to_decimal(invoices_result.value('products_total')) + \
    #                            self.convert_to_decimal(invoice['accessories']) + \
    #                            self.convert_to_decimal(invoice['above_installation'])
    #         invoices.append(invoice)
    #     invoices_dataframe = pd.DataFrame(invoices)
    #     new_columns = [column.replace('_', ' ').capitalize() for column in invoices_dataframe.columns]
    #     invoices_dataframe.rename({invoices_dataframe.columns[i]: new_columns[i] for i in range(len(new_columns))},
    #                               axis=1, inplace=True)
    #     return invoices_dataframe

    def get_invoices_dataframe(self, conditions=None):
        query = f"""
        SELECT invoice.id AS invoice_id, invoice.serial_number AS serial_number, invoice.date AS invoice_date
        FROM invoices AS invoice
        """

        placeholders = self.extract_values_from_conditions(conditions) if conditions else None
        invoices_result = self.execute_select_query(query_str=query, placeholders=placeholders)
        invoices = []
        while invoices_result.next():
            invoice = Invoice(invoice_id=invoices_result.value('invoice_id'),
                              serial_number=invoices_result.value('serial_number'),
                              date=invoices_result.value('invoice_date')).serialize_invoice(exclude=['products', 'employees_shares'])
            invoices.append(invoice)
        invoices_dataframe = pd.DataFrame(invoices)
        new_columns = [column.replace('_', ' ').capitalize() for column in invoices_dataframe.columns]
        invoices_dataframe.rename({invoices_dataframe.columns[i]: new_columns[i] for i in range(len(new_columns))},
                                  axis=1, inplace=True)
        return invoices_dataframe

    def convert_to_decimal(self, value=0, quantizer='.00'):
        if value == '' or not value:
            value = 0
        return Decimal(value).quantize(Decimal(quantizer))
