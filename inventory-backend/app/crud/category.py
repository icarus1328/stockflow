from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate

def create_category(db:Session, category: CategoryCreate):
    db_item = Category(**category.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_category(db:Session, id:int):
    category = db.query(Category).filter(Category.id == id).first()
    return category

def get_all_category(db:Session):
    category = db.query(Category).all()
    return category