from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.user import UserCreate

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def create_user(db:Session, user:UserCreate):
    hashed = hash_password(user.password)
    db_user = User(
        username = user.username,
        email = user.email,
        password_hash = hashed,
        department = user.department,
        role = user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db:Session, id:int):
    user = db.query(User).filter(User.id == id).first()
    return user

def get_user_by_email(db:Session, email:str):
    user = db.query(User).filter(User.email == email).first()
    return user

def verify_password(plain:str, hashed:str) -> bool:
    return pwd_context.verify(plain,hashed)