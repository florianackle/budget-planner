from sqlalchemy.orm import Session
from .. import models, schemas
from .user_service import get_user_by_username
from fastapi import HTTPException

def get_current_user(db: Session, username: str):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

def create_budget(db: Session, budget: schemas.BudgetCreate, user_id: int):
    db_budget = models.Budget(**budget.dict(), owner_id=user_id)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

def get_budgets(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Budget).filter(models.Budget.owner_id == user_id).offset(skip).limit(limit).all()

def get_budget(db: Session, budget_id: int, user_id: int):
    return db.query(models.Budget).filter(models.Budget.id == budget_id, models.Budget.owner_id == user_id).first()

def update_budget(db: Session, budget_id: int, budget: schemas.BudgetCreate, user_id: int):
    db_budget = get_budget(db, budget_id, user_id)
    if db_budget:
        for key, value in budget.dict().items():
            setattr(db_budget, key, value)
        db.commit()
        db.refresh(db_budget)
    return db_budget

def delete_budget(db: Session, budget_id: int, user_id: int):
    db_budget = get_budget(db, budget_id, user_id)
    if db_budget:
        db.delete(db_budget)
        db.commit()
