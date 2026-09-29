from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from .config import get_settings

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALG = "HS256"

def hash_password(value): return pwd.hash(value)
def verify_password(value, hashed): return pwd.verify(value, hashed)

def create_token(user_id):
    s = get_settings()
    exp = datetime.now(timezone.utc) + timedelta(minutes=s.access_token_expire_minutes)
    return jwt.encode({"sub": str(user_id), "exp": exp}, s.secret_key, algorithm=ALG)

def decode_token(token):
    try:
        p = jwt.decode(token, get_settings().secret_key, algorithms=[ALG])
        return int(p["sub"])
    except (JWTError, KeyError, ValueError, TypeError):
        return None
