from typing import Union

from pydantic import BaseModel


class Student(BaseModel):
    name: Union[str, None] = None
    branch: str
    age: int
    gender: str
    registration: int
    class Config:
        orm_mode = True

class Book(BaseModel):
    title: str
    department: str
    class Config:
        orm_mode = True
    