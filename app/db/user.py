from sqlalchemy import Column, Integer, String, Boolean, Enum
import enum

from app.db.base import Base

class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"
    TEST = "tester"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)