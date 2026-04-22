from sqlalchemy import Column,Integer,Float,DateTime,ForeignKey,String
from sqlalchemy.sql import func
from sqlalchemy import Enum as SAEnum
from app.database import Base
from app.models.enums import TransactionType

class InventoryTransaction(Base):
    
    __tablename__ = 'inventory_transactions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer,ForeignKey("products.id"), nullable=False)
    transaction_type = Column(SAEnum(TransactionType), nullable=False)
    quantity = Column(Integer, nullable=False)
    notes = Column(String(200), nullable=True)
    performed_by = Column(Integer,ForeignKey("users.id"),nullable=False)
    created_at = Column(DateTime(timezone=False),server_default=func.now())
    