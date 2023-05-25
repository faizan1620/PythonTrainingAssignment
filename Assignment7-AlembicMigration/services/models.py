from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    branch = Column(String)
    age = Column(Integer)
    gender = Column(String)
    registration = Column(Integer)


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    department = Column(String)
    book_id = Column(Integer, ForeignKey("student.id"))
