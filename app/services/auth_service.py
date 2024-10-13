from app.utils.security import verify_password, get_password_hash, create_access_token
from app.models.user import User
from sqlalchemy.orm import Session

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_user(db: Session, user_data):
    hashed_password = get_password_hash(user_data.password)
    user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
