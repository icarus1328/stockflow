from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.crud import inventory_transaction as crud
from app.schemas.inventory_transaction import TransactionCreate, TransactionResponse

router = APIRouter(prefix="/transaction", tags=["transaction"])

@router.post("/", response_model=TransactionResponse)
def add_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, transaction)

@router.get("/{product_id}/transaction", response_model=list[TransactionResponse])
def get_transaction(product_id: int, db: Session = Depends(get_db)):
    db_transaction = crud.get_transactions_by_product(db, product_id)
    
