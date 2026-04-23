from pydantic import BaseModel, ConfigDict, EmailStr

class SupplierCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr

class SupplierResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    phone: str
    email: EmailStr