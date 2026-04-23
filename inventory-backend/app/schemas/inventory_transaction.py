from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from app.models.enums import TransactionType

class TransactionCreate(BaseModel):
    product_id: int
    transaction_type: TransactionType
    quantity: int
    notes: Optional[str] = None
    performed_by: Optional[int] = None

class TransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    transaction_type: str
    quantity: int
    notes: Optional[str] = None
    performed_by: int
    created_at: datetime