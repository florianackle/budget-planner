from pydantic import BaseModel
from typing import List, Optional
import datetime


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class Login(BaseModel):
    username: str
    password: str


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    amount: float
    type: str
    description: str
    date: datetime.datetime
    category_id: int


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
