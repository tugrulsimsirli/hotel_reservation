from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import create_user, authenticate_user
from app.utils.security import create_access_token
from sqlalchemy.orm import Session
from app.db.base import get_db

auth_router = APIRouter()

@auth_router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user

@auth_router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

