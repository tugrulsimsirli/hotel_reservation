from fastapi import APIRouter

hotel_router = APIRouter()

@hotel_router.get("/hello")
def hello_world():
    return {"message": "Hello World!"}
