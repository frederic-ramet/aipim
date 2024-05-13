from redis import StrictRedis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings
import sqlite3


def init_db():
    """
    This method is used to create the database instance.
    :return: db instance and after complete operation, it will automatically close the session in finally.
    """
    conn = sqlite3.connect('ai-pim.db')
    db = conn.cursor()
    try:
        yield db
    finally:
        db.close()