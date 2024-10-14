from app.models.generic import ResponseModel, ErrorModel
from app.models.user_model import UserResponseModel
from app.utils.security import verify_password, get_password_hash, create_access_token
from app.db.user import User
from sqlalchemy.orm import Session

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_user(db: Session, user_data):
    existing_user = db.query(User).filter(
        (User.username == user_data.username) | (User.email == user_data.email)).first()

    if existing_user:
        error = ErrorModel(code=400, message="Username or email already registered",
                           details="A user with the given email or username already exists.")
        return ResponseModel(success=False, error=error)

    try:
        hashed_password = get_password_hash(user_data.password)

        user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)

        db.add(user)
        db.commit()
        db.refresh(user)

        return ResponseModel[UserResponseModel](success=True, data=UserResponseModel.model_validate(user))

    except Exception as e:
        error = ErrorModel(code=500, message="Internal server error", details=str(e))
        return ResponseModel(success=False, error=error)
