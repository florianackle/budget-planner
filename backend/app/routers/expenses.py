from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import Expense, ExpenseCreate
from ..services.expense_service import create_expense, get_expenses, get_expense, update_expense, delete_expense
from ..dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/expenses",
    tags=["expenses"],
)

@router.post("/", response_model=Expense)
def create_new_expense(expense: ExpenseCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return create_expense(db=db, expense=expense, user_id=current_user.id)

@router.get("/", response_model=List[Expense])
def read_all_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_expenses(db=db, user_id=current_user.id, skip=skip, limit=limit)

@router.get("/{expense_id}", response_model=Expense)
def read_single_expense(expense_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    expense = get_expense(db=db, expense_id=expense_id, user_id=current_user.id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.put("/{expense_id}", response_model=Expense)
def update_existing_expense(expense_id: int, expense: ExpenseCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return update_expense(db=db, expense_id=expense_id, expense=expense, user_id=current_user.id)

@router.delete("/{expense_id}", response_model=dict)
def delete_existing_expense(expense_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    delete_expense(db=db, expense_id=expense_id, user_id=current_user.id)
    return {"message": "Expense deleted successfully"}
