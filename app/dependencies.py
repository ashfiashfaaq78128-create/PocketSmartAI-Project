from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session
from .auth import decode_token
from .database import get_db
from .models import User

def current_user(authorization: str | None = Header(default=None), db: Session = Depends(get_db)):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(401, "Login required")
    uid = decode_token(authorization.split(" ", 1)[1])
    user = db.get(User, uid) if uid else None
    if not user:
        raise HTTPException(401, "Invalid or expired token")
    return user
