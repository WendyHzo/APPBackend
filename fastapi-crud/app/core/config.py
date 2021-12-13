from pydantic import BaseSettings
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
  API_V1_STR: str = "/api/v1"
   PROJECT_NAME: str = "Licoreria"
 
   POSTGRES_SERVER: str = "localhost"
   POSTGRES_USER: str = "fastapi"
   POSTGRES_PASSWORD: str = "123123"
   POSTGRES_DB: str = "Store"
   SQLALCHEMY_DATABASE_URI: Optional[str] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

    class Config:
        case_sensitive = True

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
