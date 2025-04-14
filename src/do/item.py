from sqlalchemy import Column, Integer, String, Float
from src.database_manager import DatabaseManager

# Get the Base class from the DatabaseManager
db_manager = DatabaseManager()
Base = db_manager.Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    unit_price = Column(Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"<Item(name='{self.name}', unit_price={self.unit_price})>"