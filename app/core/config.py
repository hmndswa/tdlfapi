from pydantic_settings import BaseSettings
from typing import Optional, Required

class Settings(BaseSettings):
    DATABASE_URL: Optional[str]

    class Config:
        env_file = '.env'

settings = Settings()