from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer
from .database import SessionLocal
from .services.user_service import get_user_by_username
from .services.jwt import decode_access_token
from jwt import DecodeError

bearer_scheme = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(bearer_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode the JWT token to extract the username
        payload = decode_access_token(token.credentials)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except DecodeError:
        raise credentials_exception

    # Find the user by the extracted username
    user = get_user_by_username(db, username=username)
    if user is None:
        raise credentials_exception
    return user
