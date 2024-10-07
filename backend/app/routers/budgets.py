from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import Budget, BudgetCreate
from ..services.budget_service import create_budget, get_budgets, get_budget, update_budget, delete_budget
from ..dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/budgets",
    tags=["budgets"],
)

@router.post("/", response_model=Budget)
def create_new_budget(budget: BudgetCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return create_budget(db=db, budget=budget, user_id=current_user.id)

@router.get("/", response_model=List[Budget])
def read_all_budgets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_budgets(db=db, user_id=current_user.id, skip=skip, limit=limit)

@router.get("/{budget_id}", response_model=Budget)
def read_single_budget(budget_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    budget = get_budget(db=db, budget_id=budget_id, user_id=current_user.id)
    if budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

@router.put("/{budget_id}", response_model=Budget)
def update_existing_budget(budget_id: int, budget: BudgetCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return update_budget(db=db, budget_id=budget_id, budget=budget, user_id=current_user.id)

@router.delete("/{budget_id}", response_model=dict)
def delete_existing_budget(budget_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    delete_budget(db=db, budget_id=budget_id, user_id=current_user.id)
    return {"message": "Budget deleted successfully"}
