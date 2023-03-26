from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config

#SQLALCHEMY_DATABASE_URL = "postgresql://localhost:5432/student"

SQLALCHEMY_DATABASE_URL = f"postgresql://{Config.db_user}:{Config.db_password}@{Config.db_server}/{Config.db_name}"

print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()