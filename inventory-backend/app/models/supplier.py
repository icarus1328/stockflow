from sqlalchemy import Column,String,Integer
from app.database import Base

class Supplier(Base):
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), unique=True,nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    
    