from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import Income, IncomeCreate
from ..services.income_service import create_income, get_incomes, get_income, update_income, delete_income
from ..dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/incomes",
    tags=["incomes"],
)


@router.post("/", response_model=Income)
def create_new_income(income: IncomeCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Check if user has a budget
    if not current_user.budget:
        raise HTTPException(status_code=400, detail="User has no budget")

    # Create income with user_id and budget_id
    return create_income(db=db, income=income, user_id=current_user.id, budget_id=current_user.budget.id)


@router.get("/", response_model=List[Income])
def read_all_incomes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_incomes(db=db, user_id=current_user.id, skip=skip, limit=limit)

@router.get("/{income_id}", response_model=Income)
def read_single_income(income_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    income = get_income(db=db, income_id=income_id, user_id=current_user.id)
    if income is None:
        raise HTTPException(status_code=404, detail="Income not found")
    return income

@router.put("/{income_id}", response_model=Income)
def update_existing_income(income_id: int, income: IncomeCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return update_income(db=db, income_id=income_id, income=income, user_id=current_user.id)

@router.delete("/{income_id}", response_model=dict)
def delete_existing_income(income_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    delete_income(db=db, income_id=income_id, user_id=current_user.id)
    return {"message": "Income deleted successfully"}
