import logging
import secrets
from datetime import timedelta
from logging.handlers import RotatingFileHandler
from typing import List
from pydantic_settings import BaseSettings
from fastapi_mail import ConnectionConfig


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
    # JWT_ACCESS_SECRET_KEY: str = secrets.token_urlsafe(32)
    # JWT_REFRESH_SECRET_KEY: str = secrets.token_urlsafe(32)
    # JWT_ALGORITHM: str = "HS256"
    # TEMPLATE_FOLDER: str = 'core/static/templates/'
    # MAIL_USERNAME: str
    # MAIL_PASSWORD: str
    # MAIL_FROM: str
    # MAIL_PORT: int
    # MAIL_SERVER: str
    # MAIL_FROM_NAME: str
    # MAIL_STARTTLS: bool = True
    # MAIL_SSL_TLS: bool = False
    # USE_CREDENTIALS: bool = True
    # RESET_PASSWORD_LINK: str
    # JWT_ACCESS_TOKEN_EXPIRES: timedelta = timedelta(minutes=60)
    # JWT_REFRESH_TOKEN_EXPIRES: timedelta = timedelta(minutes=600)
    # JWT_FORGET_PASSWORD_TOKEN_EXPIRES: timedelta = timedelta(minutes=10)
    REDIS_HOST: str
    OPENAI_API_KEY: str
    # ORG_BRANCH_NAME: str
    # ORG_GIT_USER_NAME: str
    # ORG_GIT_TOKEN: str
    # ORG_REPO_NAME: str
    # ORG_NAME: str
    # ORG_DEFAULT_APP: str
    # BASE_BRANCH_NAME: str
    # BASE_USER_NAME: str
    # BASE_REPO_NAME: str

    # SERVER_IP: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_ignore_empty = False  # It will ignore if value is not set in .env
        extra = "ignore"  # It will ignore if extra fields found in .env


# Create an instance of the Settings class
settings = Settings()


# # for email configuration
# class MailConfig:

#     @staticmethod
#     def connection_config():
#         """
#         :return: connection config object.
#         """
#         return ConnectionConfig(
#             MAIL_USERNAME=settings.MAIL_USERNAME,
#             MAIL_PASSWORD=settings.MAIL_PASSWORD,
#             MAIL_FROM=settings.MAIL_FROM,
#             MAIL_PORT=settings.MAIL_PORT,
#             MAIL_SERVER=settings.MAIL_SERVER,
#             MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
#             MAIL_STARTTLS=settings.MAIL_STARTTLS,
#             MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
#             USE_CREDENTIALS=settings.USE_CREDENTIALS,
#         )


# # File Logging Configuration
# def file_setup_logger():
#     # Set up file logging
#     file_logger_ins = logging.getLogger("file_logger")
#     file_logger_ins.setLevel(logging.INFO)

#     file_handler = RotatingFileHandler('cocon_app.log', maxBytes=10000, backupCount=5)
#     file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(file_formatter)
#     file_logger_ins.addHandler(file_handler)

#     return file_logger_ins


# # Create a file_logger instance using the file_setup_logger functions
# file_logger = file_setup_logger()
