from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime

from app.helpers.database import Base



class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)
    phone = Column(String)


    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "email": self.email,
            "phone": self.phone
        }