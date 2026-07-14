from sqlalchemy import Column, Integer, String

from app.helpers.database import Base

class Bookstore(Base):
    __tablename__ = "Bookstore"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    address = Column(String)


    def __init__(self, name, address):
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