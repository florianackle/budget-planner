from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class BudgetBase(BaseModel):
    total_amount: int = 0  # set default 0

class BudgetCreate(BudgetBase):
    pass

class Budget(BudgetBase):
    id: int
    expenses: Optional[List[int]] = []
    incomes: Optional[List[int]] = []

    model_config = ConfigDict(from_attributes=True)
