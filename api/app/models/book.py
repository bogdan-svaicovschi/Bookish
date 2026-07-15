from sqlalchemy import Column, Integer, String, ForeignKey

from app.helpers.database import Base
from app.models.genre import Genre

class Book(Base):
    __tablename__ = "Book"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique = True)
    genre = Column(Integer, ForeignKey("Genre.id"))


    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "genre": self.genre
        }
    