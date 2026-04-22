from sqlalchemy import Column,String,Integer
from app.database import Base

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)