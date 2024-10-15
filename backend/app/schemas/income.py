from datetime import datetime

from pydantic import BaseModel, ConfigDict

class IncomeBase(BaseModel):
    description: str
    amount: int
    category_id: int

class IncomeCreate(IncomeBase):
    budget_id: int

class Income(IncomeBase):
    id: int
    created_at: datetime
    budget_id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
