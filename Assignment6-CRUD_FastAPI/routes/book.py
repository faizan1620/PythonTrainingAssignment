from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import crud, models, schema
from services.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
router = APIRouter(
    prefix='/book'
)

@router.get('/')
def get_books(db: Session = Depends(get_db)):
    """
    Returns list of all books:

    """
    books = crud.get_books(db)
    if not books:
        raise HTTPException(status_code=404,detail=f"No book details found")
    return books

@router.get('/{id}')
def get_book_by_id(id:int, db: Session = Depends(get_db)):
    """
    Return only book associated with that id:

    - **id**: An integer value
    """
    book = crud.get_book_by_id(db, id)
    if not book:
        raise HTTPException(status_code=404,detail=f"Book with id: {id} doesnot exist")
    return book

@router.get('/student/{student_id}')
def get_book_by_student_id(student_id:int, db: Session = Depends(get_db)):
    """
    Returns list of all books associated with the corresponding student id:

    - **student_id**: An integer value
    """
    book = crud.get_book_by_student_id(db, student_id)
    if not book:
        raise HTTPException(status_code=404,detail=f"Book with Student id: {student_id} doesnot exist")
    return book

@router.post('/')
def post_books(book: schema.Book,  student_id:int, db: Session = Depends(get_db)):
    """
    Create a book with all the information associated to any student:

    - **student_id**: An integer value
    - **title**: Title of the book
    - **department**: Department of book
    """
    book = crud.create_student_book(db=db, book=book, student_id=student_id)
    return book


@router.delete('/{id}')
def delete_student_book(id: int,  db: Session = Depends(get_db)): 
    """
    Delete the book information for any specific id:

    - **id**: An integer value
    """
    book = crud.delete_book(db, id)
    if not book:
        raise HTTPException(404,f"Book couldnot be deleted with id: {id}")
    return {
        "detail": f"Book with id: {id} deleted successfully!",
        "status": "Success"
    }

@router.put('/{id}')
def update_student(id:int, book: schema.Book,db: Session = Depends(get_db)):
    """
    Update the book information:

    - **id**: An integer value, id of book
    - **title**: Title of the book
    - **department**: Department of book
    """
    student = crud.update_book(db,book,id)
    if not student:
        raise HTTPException(404,f"Book couldnot be updated with id: {id}")
    return book
