from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.crud.user import verify_password, get_user_by_email
from app.core.security import token_create
from app.schemas.auth import TokenResponse, LoginRequest


router = APIRouter(prefix="/authenticate", tags=["authenticate"])

@router.post("/", response_model=TokenResponse)
def login(request:LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, request.email)
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    if not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    token = token_create(user.id)
    return {"access_token": token, "token_type": "bearer"}
