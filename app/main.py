from fastapi import FastAPI
from app.api.routes.v1.auth_routes import auth_router
from app.api.routes.v1.hotel_routes import hotel_router
from app.db.base import Base, engine

application = FastAPI(
    title="Hotel Reservation API",
    description="API for managing hotel reservations, users, and more",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

application.include_router(auth_router, prefix="/auth", tags=["Authentication"])
application.include_router(hotel_router, prefix="/api/v1/hotels", tags=["Hotels"])
