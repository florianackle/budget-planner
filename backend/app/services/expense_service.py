from sqlalchemy.orm import Session
from .. import models, schemas
from .user_service import get_user_by_username
from fastapi import HTTPException

def get_current_user(db: Session, username: str):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

def create_expense(db: Session, expense: schemas.ExpenseCreate, user_id: int):
    db_expense = models.Expense(**expense.dict(), owner_id=user_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Expense).filter(models.Expense.owner_id == user_id).offset(skip).limit(limit).all()

def get_expense(db: Session, expense_id: int, user_id: int):
    return db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.owner_id == user_id).first()

def update_expense(db: Session, expense_id: int, expense: schemas.ExpenseCreate, user_id: int):
    db_expense = get_expense(db, expense_id, user_id)
    if db_expense:
        for key, value in expense.dict().items():
            setattr(db_expense, key, value)
        db.commit()
        db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int, user_id: int):
    db_expense = get_expense(db, expense_id, user_id)
    if db_expense:
        db.delete(db_expense)
        db.commit()
