from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.crud import user as crud
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/{id}", response_model=UserResponse)
def get_user_id(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user
