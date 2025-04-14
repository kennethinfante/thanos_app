from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.database_manager import DatabaseManager

# Get the Base class from the DatabaseManager
db_manager = DatabaseManager()
Base = db_manager.Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_person = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String, nullable=False)
    website = Column(String)
    tax_number = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    description = Column(String)
    is_active = Column(String)
    created_at = Column(DateTime, nullable=False)

    # Define relationships
    invoices = relationship("Invoice", back_populates="customer")

    def __repr__(self):
        return f"<Customer(name='{self.name}', email='{self.email}')>"