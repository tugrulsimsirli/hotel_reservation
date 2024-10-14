from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.models.generic import ResponseModel
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import create_user, authenticate_user
from app.utils.security import create_access_token, create_refresh_token, decode_refresh_token
from sqlalchemy.orm import Session
from app.db.base import get_db

auth_router = APIRouter()
@auth_router.post("/signup", response_model=ResponseModel)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    if not db_user.success:
        return JSONResponse(status_code=db_user.error.code, content=db_user.dict())

    return db_user

@auth_router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token, exp = create_access_token(data={"sub": user.username})
    ref_token = create_refresh_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "refresh_token": ref_token,
        "token_type": "bearer",
        "user_id": user.id,
        "expired_at": exp
    }

@auth_router.post("/refresh_token")
def refresh_token(ref_token: str):
    payload, is_valid = decode_refresh_token(ref_token)
    if not is_valid:
        raise HTTPException(status_code=400, detail="Invalid token")
    access_token, exp = create_access_token(data={"sub": payload.get("sub")})
    ref_token = create_refresh_token(data={"sub": payload.get("sub")})
    return {
        "access_token": access_token,
        "refresh_token": ref_token,
        "token_type": "bearer",
        "user_id": payload.get("sub"),
        "expired_at": exp
    }

