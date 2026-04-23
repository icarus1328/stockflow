from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    department: str
    role: str
    
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: EmailStr
    department: str
    role: str
    is_active: bool
    created_at: datetime
    
class UserInDB(UserResponse):
    password_hash: str