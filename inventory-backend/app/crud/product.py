from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.products import ProductCreate

def create_product(db:Session, product:ProductCreate):
    db_product = Product(
        name = product.name,
        category_id = product.category_id,
        buying_price = product.buying_price,
        selling_price = product.selling_price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db:Session, id:int):
    product = db.query(Product).filter(Product.id == id).first()
    return product

def get_all_product(db:Session):
    product = db.query(Product).all()
    return product

