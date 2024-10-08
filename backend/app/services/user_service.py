from sqlalchemy.orm import Session
from .. import models, schemas
from passlib.context import CryptContext
from ..services.budget_service import create_budget_for_user
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def register_user(db: Session, user: schemas.UserCreate):
    db_user = create_user(db=db, user=user)

    # create budget for user after user is created
    try:
        create_budget_for_user(db=db, user_id=db_user.id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Budget creation failed")

    return db_user
