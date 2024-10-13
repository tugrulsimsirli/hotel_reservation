from pydantic_settings import BaseSettings

class DatabaseSettings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/hotel_reservation"

class AuthSettings(BaseSettings):
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 20160 # 1 week

class Settings(BaseSettings):
    PROJECT_NAME: str = "Hotel Reservation API"
    DATABASE: DatabaseSettings = DatabaseSettings()
    AUTH: AuthSettings = AuthSettings()

settings = Settings()
