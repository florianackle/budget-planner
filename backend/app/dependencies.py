from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .services.user_service import get_user_by_username

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(username: str, db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=username)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
