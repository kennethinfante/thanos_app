from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database_manager import DatabaseManager

# Get the Base class from the DatabaseManager
db_manager = DatabaseManager()
Base = db_manager.Base

class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    # here the ForeignKey specifies the table name as found in db
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    invoice_number = Column(String, unique=True, nullable=False)
    date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    subtotal = Column(Float, nullable=False, default=0.0)
    tax_amount = Column(Float, nullable=False, default=0.0)
    total_amount = Column(Float, nullable=False, default=0.0)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False, default='unpaid')
    created_at = Column(DateTime, nullable=False)

    # Define relationships
    # for consistency, just singular
    customer = relationship("Customer", back_populates="invoices", uselist=False)

    # Add relationship to invoice lines
    invoice_lines = relationship("InvoiceLine", back_populates="invoice", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Invoice(customer='{self.customer.name}', amount='{self.total_amount}')>"


class InvoiceLine(Base):
    __tablename__ = 'invoice_lines'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=True)
    description = Column(String, nullable=False)
    quantity = Column(Float, nullable=False, default=1.0)
    unit_price = Column(Float, nullable=False, default=0.0)
    tax_rate_id = Column(Integer, ForeignKey('tax_rates.id'), nullable=False)
    subtotal = Column(Float, nullable=False, default=0.0)
    tax_amount = Column(Float, nullable=False, default=0.0)
    line_amount = Column(Float, nullable=False, default=0.0)

    # Define relationships
    invoice = relationship("Invoice", back_populates="invoice_lines")
    item = relationship("Item", uselist=False)
    account = relationship("Account", uselist=False)
    tax_rate = relationship("TaxRate", uselist=False)

    def __repr__(self):
        return f"Invoice #: {self.invoice_id}, Amount: {self.line_amount}"