from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config

# SQLALCHEMY_DATABASE_URL = "postgresql://localhost:5432/student"
SQLALCHEMY_DATABASE_URL = f"postgresql://{config.db_user}:{config.db_password}@{config.db_server}/{config.db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
