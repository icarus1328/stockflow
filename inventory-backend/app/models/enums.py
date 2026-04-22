from enum import Enum

class TransactionType(str, Enum):
    stock_in = 'stock_in'
    stock_out = 'stock_out'