from sqlalchemy.orm import Session
from app.models.supplier import Supplier
from app.schemas.suppliers import SupplierCreate

def create_supplier(db:Session, supplier:SupplierCreate):
    db_supplier = Supplier(
        name = supplier.name,
        phone = supplier.phone,
        email = supplier.email
    )
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def get_supplier_by_id(db:Session, id:int):
    supplier = db.query(Supplier).filter(Supplier.id == id).first()
    return supplier

def get_all_supplier(db:Session):
    supplier = db.query(Supplier).all()
    return supplier
