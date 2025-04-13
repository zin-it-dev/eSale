from os import environ
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base

load_dotenv()

username = environ.get("DB_USER")
password = environ.get("DB_PASSWORD")
name = environ.get("DB_NAME")
port = environ.get("DB_PORT")
host = environ.get("DB_HOST")

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{name}?charset=utf8mb4",
    echo=True,
    pool_size=10,
)


def init_db():
    Base.metadata.create_all(engine)


def get_session():
    return Session(engine)


if __name__ == "__main__":
    init_db()
