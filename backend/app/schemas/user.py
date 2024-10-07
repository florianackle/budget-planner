from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    budgets: Optional[List[int]] = []

    model_config = ConfigDict(from_attributes=True)
