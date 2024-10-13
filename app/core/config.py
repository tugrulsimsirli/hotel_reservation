from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/hotel_reservation"
    PROJECT_NAME: str = "Hotel Reservation API"

settings = Settings()
