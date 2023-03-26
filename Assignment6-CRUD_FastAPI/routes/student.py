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
    prefix='/student'
)

@router.get('/')
def get_students(db: Session = Depends(get_db)):
    """
    Returns list of all students:

    """
    students = crud.get_students(db)
    if not students:
        raise HTTPException(status_code=404,detail=f"No data found")
    return students

@router.get('/{id}')
def get_student_by_id(id:int, db: Session = Depends(get_db)):
    """
    Return only student associated with that id:

    - **id**: An integer value
    """
    student = crud.get_student_by_id(db,id)
    if not student:
        raise HTTPException(status_code=404,detail=f"Student with id: {id} doesnot exist")
    return student

@router.post('/')
def post_students(student: schema.Student,db: Session = Depends(get_db)):
    """
    Create a student with all the information:

    - **name**: Name of the student, string value
    - **branch**: Branch of the student, string value
    - **age**: Age of the student, integer value
    - **gender**: Gender of student, string value
    - **registration**: An integer value
    """
    student = crud.create_student(db=db, student=student)
    return student


@router.delete('/{id}')
def delete_students(id:int,db: Session = Depends(get_db)):
    """
    Delete the student information for any specific id:

    - **id**: An integer value
    """
    student = crud.delete_student(db, id)
    if not student:
        raise HTTPException(404,f"Student couldnot be deleted with id: {id}")
    return {
        "detail": f"Student with id: {id} deleted successfully!",
        "status": "Success"
    }

@router.put('/{id}')
def update_student(id:int, student: schema.Student,db: Session = Depends(get_db)):
    """
    Update a student with all the information for specific id:

    - **id**: Integer value, id of the student
    - **name**: Name of the student, string value
    - **branch**: Branch of the student, string value
    - **age**: Age of the student, integer value
    - **gender**: Gender of student, string value
    - **registration**: An integer value
    """
    student = crud.update_student(db,student,id)
    if not student:
        raise HTTPException(404,f"Student couldnot be updated with id: {id}")
    return student
