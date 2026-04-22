from sqlalchemy import Column,Integer,ForeignKey
from app.database import Base

class ProductSupplier(Base):
    
    __tablename__ = "product_suppliers"
    
    product_id = Column(Integer,ForeignKey("products.id"),nullable=False)
    supplier_id = Column(Integer,ForeignKey("suppliers.id"),nullable=False)