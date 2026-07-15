from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime

from app.helpers.database import Base
from app.models.book import Book
from app.models.author import Author


class IntellectualProperty(Base):
    __tablename__ = "IntellectualProperty"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    book = Column(Integer, ForeignKey("Book.id"))
    author = Column(Integer, ForeignKey("Author.id"))


    def __init__(self, name, ):
        self.name = name
        self.address = address

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
    