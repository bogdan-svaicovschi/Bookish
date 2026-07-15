from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as SessionType

from app.dependencies import get_db
from app.schemas.example import ExampleCreate
from app.models.example import Example
from app.models.book import Book
from app.schemas.book import BookCreate
from app.models.genre import Genre
 
router = APIRouter(tags=["health"])

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/example", response_model=ExampleCreate)
def create_example(example: ExampleCreate, db: SessionType = Depends(get_db)):
    db_example = Example(example_field_1=example.example_field_1, example_field_2=example.example_field_2)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

@router.post("/book", response_model=BookCreate)
def create_book(book: BookCreate, db: SessionType = Depends(get_db)):
    db_example = Book(name = book.name, genre = book.genre)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

@router.get("/book")
def return_book(db: SessionType = Depends(get_db)):
    return db.query(Book).all()


@router.post("/generate-genres")
def generate_genres(db: SessionType = Depends(get_db)):
    db.add(Genre("History"))
    db.add(Genre("Politics"))
    db.add(Genre("Romance"))
    db.add(Genre("Sci-fi"))
    db.add(Genre("Personal Development"))
    db.add(Genre("Economics"))
    db.add(Genre("Psychology"))
    db.commit()
    return {"status": "ok"}

@router.post("/delete-genres")
def generate_genres(db: SessionType = Depends(get_db)):
    db.query(Genre).delete()
    db.commit()
    return {"status": "ok"}

@router.get("/genre")
def return_book(db: SessionType = Depends(get_db)):
    return db.query(Genre).all()

