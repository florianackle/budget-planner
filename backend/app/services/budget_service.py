from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException

def get_current_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user ID")
    return user


def create_budget_for_user(db: Session, user_id: int):
    db_budget = models.Budget(total_amount=0, owner_id=user_id)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

def get_user_budget(db: Session, user_id: int):
    # Get budget of current user
    return db.query(models.Budget).filter(models.Budget.owner_id == user_id).first()

def update_budget(db: Session, budget: schemas.BudgetCreate, user_id: int):
    # Update budget of the current user
    db_budget = get_user_budget(db, user_id)
    if db_budget:
        for key, value in budget.model_dump().items():
            setattr(db_budget, key, value)
        db.commit()
        db.refresh(db_budget)
    return db_budget

def delete_budget(db: Session, user_id: int):
    # Delete budget of the current user
    db_budget = get_user_budget(db, user_id)
    if db_budget:
        db.delete(db_budget)
        db.commit()
