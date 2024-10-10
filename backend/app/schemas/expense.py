from datetime import datetime

from pydantic import BaseModel, ConfigDict

class ExpenseBase(BaseModel):
    description: str
    amount: int
    category_id: int

class ExpenseCreate(ExpenseBase):
    budget_id: int

class Expense(ExpenseBase):
    id: int
    created_at: datetime
    budget_id: int
    owner_id: int

    class Config:
        orm_mode = True
