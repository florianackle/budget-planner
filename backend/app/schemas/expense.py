from pydantic import BaseModel, ConfigDict

class ExpenseBase(BaseModel):
    description: str
    amount: int
    category_id: int

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    budget_id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
