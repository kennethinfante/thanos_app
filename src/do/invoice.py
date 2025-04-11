from datetime import datetime, date
from dataclasses import dataclass, field

@dataclass
class Invoice:
    id: int
    customer_id: int
    invoice_number: str
    date: date
    due_date: date
    subtotal: float
    tax_amount: float
    total_amount: float
    description: str = None
    status: str = 'unpaid'
    created_at: datetime = field(default_factory=lambda: datetime.now())
    # self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.invoice_number

    def serialize_invoice(self, fields='All', exclude=None):
        if fields == 'All':
            data = self.__dict__.copy()
        else:
            data = {field: getattr(self, field) for field in fields}

        if exclude:
            for field_ in exclude:
                data.pop(field_, None)

        return data
