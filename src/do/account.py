from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database_manager import DatabaseManager

# Get the Base class from the DatabaseManager
db_manager = DatabaseManager()
Base = db_manager.Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    account_type_id = Column(Integer, nullable=False)
    parent_type_id = Column(Integer)
    is_active = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Account(code='{self.code}', name='{self.name}')>"