from fastapi import FastAPI
from app.api.routes.v1.auth_routes import auth_router
from app.api.routes.v1.hotel_routes import hotel_router
from app.db.base import Base, engine
from app.middlewares.error_handler import global_exception_handler

application = FastAPI(
    title="Hotel Reservation API",
    description="API for managing hotel reservations, users, and more",
    version="1.0.0"
)

application.middleware("http")(global_exception_handler)

Base.metadata.create_all(engine)

application.include_router(auth_router, prefix="/auth", tags=["Authentication"])
application.include_router(hotel_router, prefix="/api/v1/hotels", tags=["Hotels"])