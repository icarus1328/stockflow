from sqlalchemy import Column,Integer,String,DateTime,Boolean
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50),nullable=False,unique=True)
    email = Column(String(100), nullable=False,unique=True)
    password_hash = Column(String(200), nullable=False)
    department = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=False), server_default=func.now())