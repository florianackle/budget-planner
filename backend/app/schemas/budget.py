from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class BudgetBase(BaseModel):
    name: str
    total_amount: int

class BudgetCreate(BudgetBase):
    pass

class Budget(BudgetBase):
    id: int
    expenses: Optional[List[int]] = []
    incomes: Optional[List[int]] = []

    model_config = ConfigDict(from_attributes=True)
