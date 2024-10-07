from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import Category, CategoryCreate
from ..services.category_service import create_category, get_categories, get_category, update_category, delete_category
from ..dependencies import get_db

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@router.post("/", response_model=Category)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db=db, category=category)

@router.get("/", response_model=List[Category])
def read_all_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_categories(db=db, skip=skip, limit=limit)

@router.get("/{category_id}", response_model=Category)
def read_single_category(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db=db, category_id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=Category)
def update_existing_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    return update_category(db=db, category_id=category_id, category=category)

@router.delete("/{category_id}", response_model=dict)
def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    delete_category(db=db, category_id=category_id)
    return {"message": "Category deleted successfully"}
