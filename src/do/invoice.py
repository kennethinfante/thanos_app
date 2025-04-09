from datetime import datetime, date

class Invoice(object):
    def __init__(self, id, customer_id, invoice_number, date, due_date, subtotal, tax_amount, total_amount, description=None, status='unpaid'):
        self.id = id
        self.customer_id = customer_id
        self.invoice_number = invoice_number
        self.date = date
        self.due_date = due_date
        self.subtotal = subtotal
        self.tax_amount = tax_amount
        self.total_amount = total_amount
        self.description = description
        self.status = status
        # self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.invoice_number

    def serialize_invoice(self, fields='All', exclude=None):
        keys_to_be_excluded = list(set(self.__dict__.keys()) - set(fields)) if fields != 'All' else []
        keys_to_be_excluded.extend(exclude) if exclude else None
        for key in keys_to_be_excluded:
            del self.__dict__[key]
        return self.__dict__
