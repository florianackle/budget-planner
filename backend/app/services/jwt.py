import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET_KEY")

if not SECRET:
    SECRET = "HalloPhilippThisIsSecret"
    # raise ValueError("SECRET_KEY ist in der .env Datei nicht gesetzt")


def create_access_token(username: str):
    encoded_jwt = jwt.encode({"sub": username}, SECRET, algorithm="HS256")
    return encoded_jwt


def decode_access_token(token: str):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
