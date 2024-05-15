
from typing import List
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    PROJECT_NAME: str = "ForgeAI Backend"
    API_VERSION_STR: str = "/api/v1"
    PROJECT_DESCRIPTION: str = (
        "ForgeAI is an innovative experimentation platform built with Python, "
        "designed to facilitate the rapid setup of development environments "
        "for generative AI applications."
    )
    PROJECT_VERSION: str = "V2"
    ALLOWED_HOSTS: List[str] = [
        "http://localhost",
        "http://localhost:8000",
        "https://your.production.domain",
    ]
    SQLITE_DB_URL: str

    REDIS_HOST: str
    OPENAI_API_KEY: str


    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_ignore_empty = False  # It will ignore if value is not set in .env
        extra = "ignore"  # It will ignore if extra fields found in .env


# Create an instance of the Settings class
settings = Settings()

