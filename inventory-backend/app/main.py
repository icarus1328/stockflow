from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.routers import category, product, supplier, user, inventory_transaction, auth

app  = FastAPI(title="Inventory Management System", swagger_ui_init_oauth={})

app.include_router(category.router)
app.include_router(product.router)
app.include_router(supplier.router)
app.include_router(user.router)
app.include_router(inventory_transaction.router)
app.include_router(auth.router)