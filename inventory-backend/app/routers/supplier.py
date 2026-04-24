from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.crud import supplier as crud
from app.schemas.suppliers import SupplierCreate, SupplierResponse

router = APIRouter(prefix="/supplier", tags=["supplier"])

@router.post("/", response_model=SupplierResponse)
def add_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    return crud.create_supplier(db, supplier)

@router.get("/{id}", response_model=SupplierResponse)
def get_supplier(id: int, db: Session = Depends(get_db)):
    db_supplier = crud.get_supplier_by_id(db, id)
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Supplier Not Found")
    return db_supplier

@router.get("/", response_model=list[SupplierResponse])
def get_supplier_all(db: Session = Depends(get_db)):
    db_supplier = crud.get_all_supplier(db)
    return db_supplier
