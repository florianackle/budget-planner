from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import Budget, BudgetCreate
from ..services.budget_service import get_user_budget, create_budget_for_user, update_budget, delete_budget
from ..dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/budget",
    tags=["budget"],
)

@router.get("/", response_model=Budget)
def read_user_budget(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    budget = get_user_budget(db=db, user_id=current_user.id)
    if not budget:
        raise HTTPException(status_code=404, detail="No budget found for the user.")
    return budget

@router.post("/", response_model=Budget)
def create_new_budget(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return create_budget_for_user(db=db, user_id=current_user.id)


@router.delete("/", response_model=dict)
def delete_existing_budget(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    delete_budget(db=db, user_id=current_user.id)
    return {"message": "Budget deleted successfully"}
