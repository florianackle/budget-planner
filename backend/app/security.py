from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jwt import DecodeError
from app.services.jwt import decode_access_token as decode_access_token

bearer_scheme = HTTPBearer()


def decode_token(token: str = Depends(bearer_scheme)) -> dict:
    try:
        return decode_access_token(token.credentials)
    except DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")
    