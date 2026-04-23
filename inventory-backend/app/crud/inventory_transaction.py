from sqlalchemy.orm import Session
from app.models.inventory_transaction import InventoryTransaction
from app.schemas.inventory_transaction import TransactionCreate

def create_transaction(db:Session, transaction:TransactionCreate):
    db_transaction = InventoryTransaction(
        product_id = transaction.product_id,
        transaction_type = transaction.transaction_type,
        quantity = transaction.quantity,
        notes = transaction.notes,
        performed_by = transaction.performed_by
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions_by_product(db:Session, product_id:int):
    transaction = db.query(InventoryTransaction).filter(InventoryTransaction.product_id == product_id).all()
    return transaction

