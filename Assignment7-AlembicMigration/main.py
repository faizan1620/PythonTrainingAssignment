from fastapi import FastAPI
from routes import student, book


description = """
This API helps you do awesome stuff. 🚀

## Student

You can **read Student details and put the details of new students**.

## Book

You can assign any book to any student
"""


tags_metadata = [
    {
        "name": "Student",
        "description": "Operations with student. Do CRUD operations for Student",
    },
    {
        "name": "Book",
        "description": "Manage book for any student. ",
    },
]


app = FastAPI(title="Student Management System",
    description=description,
    version="0.0.1",openapi_tags=tags_metadata)

app.include_router(student.router, tags=["Student"])

app.include_router(book.router, tags=["Book"])

@app.get('/')
def root():
    return { 'status': 'FastAPI is running' }