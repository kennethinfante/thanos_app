from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database_manager import DatabaseManager

# Get the Base class from the DatabaseManager
db_manager = DatabaseManager()
Base = db_manager.Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    sale_price = Column(Float, nullable=False, default=0.0)
    purchase_price = Column(Float, nullable=True)
    tax_rate_id = Column(Integer, ForeignKey('tax_rates.id'), nullable=False)
    is_active = Column(Integer, nullable=False)
    inventory_tracking = Column(Integer, nullable=False)
    is_consumable = Column(Integer, nullable=False)
    is_service = Column(Integer, nullable=False)
    current_stock = Column(Float, nullable=True)
    reorder_level = Column(Float, nullable=True)
    inventory_account_id = Column(Float, ForeignKey('accounts.id'), nullable=True)
    revenue_account_id = Column(Float, ForeignKey('accounts.id'), nullable=True)
    expense_account_id = Column(Float, ForeignKey('accounts.id'), nullable=True)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Item(name='{self.name}', sale_price={self.sale_price}, purchase_price={self.purchase_price})>"