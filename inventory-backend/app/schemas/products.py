from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    category_id: int
    buying_price: float
    selling_price: Optional[float] = None
    
class ProductResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id: int
    name: str
    category_id: int
    buying_price: float
    selling_price: Optional[float] = None
    created_at: datetime