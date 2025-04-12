from datetime import datetime, date
from dataclasses import dataclass, field

@dataclass
class Item:
    id: int
    name: str
    tax_rate_id: int
    is_active: int
    inventory_tracking: int = 0
    is_consumable: int = 0
    is_service: int = 0
    description: str = None
    sale_price: float = 0.0
    purchase_price: float = None
    current_stock: int = None
    reorder_level: int = None
    inventory_account_id: int = None
    revenue_account_id: int = None
    expense_account_id: int = None
    created_at: datetime = field(default_factory=lambda: datetime.now())
    # self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.name

    def serialize_item(self, fields='All', exclude=None):
        if fields == 'All':
            data = self.__dict__.copy()
        else:
            data = {field: getattr(self, field) for field in fields}

        if exclude:
            for field_ in exclude:
                data.pop(field_, None)

        return data
