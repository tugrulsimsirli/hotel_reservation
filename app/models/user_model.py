from pydantic import BaseModel

class UserResponseModel(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }
