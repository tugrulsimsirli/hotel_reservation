from pydantic import BaseModel
from typing import Optional, Generic, TypeVar

T = TypeVar("T", bound=BaseModel)

class ErrorModel(BaseModel):
    code: int
    message: Optional[str] = None
    details: Optional[str] = None

class ResponseModel(Generic[T], BaseModel):
    success: bool
    data: Optional[T] = None
    error: Optional[ErrorModel] = None
