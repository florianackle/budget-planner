from sqlalchemy.orm import Session
from .. import models, schemas
from .user_service import get_user_by_username
from fastapi import HTTPException

def get_current_user(db: Session, username: str):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

def create_income(db: Session, income: schemas.IncomeCreate, user_id: int, budget_id: int):
    db_income = models.Income(**income.dict(), owner_id=user_id, budget_id=budget_id)
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

def get_incomes(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Income).filter(models.Income.owner_id == user_id).offset(skip).limit(limit).all()

def get_income(db: Session, income_id: int, user_id: int):
    return db.query(models.Income).filter(models.Income.id == income_id, models.Income.owner_id == user_id).first()

def update_income(db: Session, income_id: int, income: schemas.IncomeCreate, user_id: int):
    db_income = get_income(db, income_id, user_id)
    if db_income:
        for key, value in income.dict().items():
            setattr(db_income, key, value)
        db.commit()
        db.refresh(db_income)
    return db_income

def delete_income(db: Session, income_id: int, user_id: int):
    db_income = get_income(db, income_id, user_id)
    if db_income:
        db.delete(db_income)
        db.commit()
