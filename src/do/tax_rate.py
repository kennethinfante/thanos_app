from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database_manager import DatabaseManager

# Get the Base class from the DatabaseManager
db_manager = DatabaseManager()
Base = db_manager.Base

class TaxRate(Base):
    __tablename__ = 'tax_rates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    description = Column(String)
    is_active = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Account(code='{self.code}', name='{self.name}')>"