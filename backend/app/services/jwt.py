import jwt

SECRET = "ThisIsASecret"


def create_access_token(user_id: int):
    encoded_jwt = jwt.encode({"user_id": user_id}, SECRET, algorithm="HS256")
    return encoded_jwt


def decode_access_token(token: str):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
