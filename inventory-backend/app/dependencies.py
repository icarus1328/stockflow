from app.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from app.core.security import verify_token
from app.crud.user import get_user_by_id
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authenticate")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user_id = payload.get("sub")
    user = get_user_by_id(db, int(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")
    return user
