from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..auth import create_token, hash_password, verify_password
from ..database import get_db
from ..models import User
from ..schemas import RegisterRequest, LoginRequest, TokenResponse, UserResponse

router=APIRouter()
@router.post("/register",response_model=UserResponse,status_code=201)
def register(data:RegisterRequest,db:Session=Depends(get_db)):
    email=data.email.lower()
    if db.scalar(select(User).where(User.email==email)): raise HTTPException(409,"Email is already registered")
    u=User(name=data.name.strip(),email=email,password_hash=hash_password(data.password)); db.add(u); db.commit(); db.refresh(u); return u

@router.post("/login",response_model=TokenResponse)
def login(data:LoginRequest,db:Session=Depends(get_db)):
    u=db.scalar(select(User).where(User.email==data.email.lower()))
    if not u or not verify_password(data.password,u.password_hash): raise HTTPException(401,"Invalid email or password")
    return {"access_token":create_token(u.id),"token_type":"bearer"}

@router.post("/logout")
def logout(): return {"message":"Logged out on client"}
