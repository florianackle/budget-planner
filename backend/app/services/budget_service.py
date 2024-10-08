from sqlalchemy.orm import Session
from .. import models, schemas
from .user_service import get_user_by_username
from fastapi import HTTPException

def get_current_user(db: Session, username: str):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

def create_budget_for_user(db: Session, user_id: int):
    # default budget with total amount = 0
    default_budget = schemas.BudgetCreate(name="Default Budget", total_amount=0)
    db_budget = models.Budget(**default_budget.dict(), owner_id=user_id)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

def get_user_budget(db: Session, user_id: int):
    return db.query(models.Budget).filter(models.Budget.owner_id == user_id).first()

def update_budget(db: Session, budget_id: int, budget: schemas.BudgetCreate, user_id: int):
    db_budget = get_user_budget(db, user_id)
    if db_budget:
        for key, value in budget.dict().items():
            setattr(db_budget, key, value)
        db.commit()
        db.refresh(db_budget)
    return db_budget

def delete_budget(db: Session, budget_id: int, user_id: int):
    db_budget = get_user_budget(db, user_id)
    if db_budget:
        db.delete(db_budget)
        db.commit()
