from redis import StrictRedis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Create the SQLAlchemy engine
engine = create_engine(settings.POSTGRES_DB_URL, echo=False)

# Create the session maker object
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Define the declarative base
Base = declarative_base()


def init_db():
    """
    This method is used to create the database instance.
    :return: db instance and after complete operation, it will automatically close the session in finally.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_redis_client():
    redis_client = StrictRedis(host=settings.REDIS_HOST, port=6379, db=0)
    try:
        yield redis_client
    finally:
        redis_client.close()
