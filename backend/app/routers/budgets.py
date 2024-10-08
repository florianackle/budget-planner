from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import Budget, BudgetCreate
from ..services.budget_service import get_user_budget, update_budget, delete_budget
from ..dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/budgets",
    tags=["budgets"],
)

@router.get("/", response_model=Budget)
def read_user_budget(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Show budget of the current user
    budget = get_user_budget(db=db, user_id=current_user.id)
    if not budget:
        raise HTTPException(status_code=404, detail="No budget found for the user.")
    return budget

@router.put("/", response_model=Budget)
def update_existing_budget(budget: BudgetCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Update the budget of the current user
    return update_budget(db=db, budget=budget, user_id=current_user.id)

@router.delete("/", response_model=dict)
def delete_existing_budget(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Delete the budget of the current user
    delete_budget(db=db, user_id=current_user.id)
    return {"message": "Budget deleted successfully"}
