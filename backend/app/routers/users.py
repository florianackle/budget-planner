from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import User, UserCreate
from ..services.user_service import create_user, get_user_by_username
from ..services.budget_service import create_budget_for_user
from ..dependencies import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", response_model=User)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # create user
    new_user = create_user(db=db, user=user)

    # create budget for user
    create_budget_for_user(db=db, user_id=new_user.id)

    return new_user
