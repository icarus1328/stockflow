from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,Float
from sqlalchemy.sql import func
from app.database import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"),nullable=False)
    buying_price = Column(Float, nullable=False)
    selling_price = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=False), server_default=func.now())