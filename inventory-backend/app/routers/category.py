from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.crud import category as crud
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@router.get("/{id}", response_model=CategoryResponse)
def get_category(id:int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category Not Found")
    return db_category

@router.get("/", response_model=list[CategoryResponse])
def get_category_all(db:Session = Depends(get_db)):
    db_category = crud.get_all_category(db)
    return db_category
