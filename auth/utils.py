from auth.config import auth_config
from jose import jwt
from datetime import datetime, timedelta
import bcrypt


def create_token(data: dict):
    data["exp"] = datetime.utcnow() + timedelta(minutes=auth_config.EXP_TIME)
    return jwt.encode(data,auth_config.SECRET_KEY, auth_config.ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, auth_config.SECRET_KEY, auth_config.ALGORITHM)

def create_hash(password: str):
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")


def check_hash(hashed: str, entered_password: str) -> bool:
    hashed_bytes = hashed.encode('utf-8')
    entered_bytes = entered_password.encode('utf-8')
    return bcrypt.checkpw(entered_bytes, hashed_bytes)

