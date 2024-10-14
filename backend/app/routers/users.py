from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import User, UserCreate, Token
from ..services.user_service import register_user, get_user_by_username, authenticate_user
from ..services.jwt import create_access_token
from ..dependencies import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=User)
def register_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    return register_user(db=db, user=user)


@router.post("/login", response_model=Token)
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, username=user.username, password=user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(username=db_user.username)
    return {"access_token": access_token, "token_type": "bearer"}
