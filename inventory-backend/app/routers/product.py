from fastapi import APIRouter,  Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.crud import product as crud
from app.schemas.products import ProductCreate, ProductResponse
from app.models.users import User

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_product(db, product)

@router.get("/{id}", response_model=ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product Not Found")
    return db_product

@router.get("/", response_model=list[ProductResponse])
def get_product_all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_product = crud.get_all_product(db)
    return db_product