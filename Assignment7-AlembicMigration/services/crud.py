from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schema
from typing import Union


def get_student_by_id(db: Session, student_id: int) -> schema.Student:
    try:
        return db.query(models.Student).filter(models.Student.id == student_id).first()
    except Exception as e:
        raise HTTPException(400, str(e))


def get_students(db: Session, skip: int = 0, limit: int = 100) -> schema.Student:
    try:
        return db.query(models.Student).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(400, str(e))


def create_student(db: Session, student: schema.Student) -> schema.Student:
    try:
        db_student = models.Student(
            name=student.name,
            branch=student.branch,
            age=student.age,
            gender=student.gender,
            registration=student.registration,
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        raise HTTPException(400, str(e))


def update_student(
    db: Session, student: schema.Student, student_id: int
) -> schema.Student:
    try:
        db.query(models.Student).filter(models.Student.id == student_id).update(
            {
                models.Student.name: student.name,
                models.Student.branch: student.branch,
                models.Student.age: student.age,
                models.Student.gender: student.gender,
                models.Student.registration: student.registration,
            }
        )
        db.commit()
        return get_student_by_id(db, student_id)
    except Exception as e:
        raise HTTPException(400, str(e))


def delete_student(db: Session, student_id: int) -> schema.Student:
    try:
        db_student = (
            db.query(models.Student).filter(models.Student.id == student_id).delete()
        )
        db.commit()
        return db_student
    except Exception as e:
        raise HTTPException(400, str(e))


def get_books(db: Session, skip: int = 0, limit: int = 100) -> schema.Student:
    try:
        return db.query(models.Book).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(400, str(e))


def create_student_book(
    db: Session, book: schema.Book, student_id: int
) -> schema.Student:
    try:
        db_student_book = models.Book(**book.dict(), book_id=student_id)
        db.add(db_student_book)
        db.commit()
        db.refresh(db_student_book)
        return db_student_book
    except Exception as e:
        raise HTTPException(400, str(e))


def get_book_by_id(db: Session, book_id: int) -> schema.Student:
    try:
        return db.query(models.Book).filter(models.Book.id == book_id).first()
    except Exception as e:
        raise HTTPException(400, str(e))


def get_book_by_student_id(db: Session, book_id: int) -> schema.Student:
    try:
        return db.query(models.Book).filter(models.Book.book_id == book_id).all()
    except Exception as e:
        raise HTTPException(400, str(e))


def update_book(db: Session, book: schema.Book, book_id: int) -> schema.Student:
    try:
        db_book = (
            db.query(models.Book)
            .filter(models.Book.id == book_id)
            .update({**book.dict()})
        )
        db.commit()
        return db_book
    except Exception as e:
        raise HTTPException(400, str(e))


def delete_book(db: Session, book_id: int) -> schema.Student:
    try:
        db_book = db.query(models.Book).filter(models.Book.id == book_id).delete()
        db.commit()
        return db_book
    except Exception as e:
        raise HTTPException(400, str(e))
