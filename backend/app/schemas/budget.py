from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from .income import Income
from .expense import Expense

class BudgetBase(BaseModel):
    total_amount: int = 0  # set default 0

class BudgetCreate(BudgetBase):
    pass

class Budget(BudgetBase):
    id: int
    expenses: Optional[List[Income]] = []
    incomes: Optional[List[Expense]] = []

    class Config:
        orm_mode = True
