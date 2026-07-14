from sqlalchemy import Column, Integer, String, ForeignKey

from app.helpers.database import Base
from app.models.publisher import Publisher
from app.models.bookstore import Bookstore

class Edition(Base):
    __tablename__ = "Edition"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    publisher = Column(Integer, ForeignKey("Publisher.id"))
    year = Column(Integer)
    quantity = Column(Integer)
    bookstore = Column(Integer, ForeignKey("Bookstore.id"))


    def __init__(self, name, publisher, year, quantity, bookstore):
        self.name = name
        self.publisher = publisher
        self.year = year
        self.quantity = quantity
        self.bookstore = bookstore

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "publisher": self.publisher,
            "year": self.year,
            "quantity": self.quantity,
            "bookstore": self.bookstore

        }
    