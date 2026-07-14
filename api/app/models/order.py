from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime

from app.helpers.database import Base
from app.models.user import User


class Order(Base):
    __tablename__ = "Order"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String)
    date = Column(datetime)
    user = Column(Integer, ForeignKey("User.id"))


    def __init__(self, status, date, user):
        self.status = status
        self.date = date
        self.user = user

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "user": self.user,
            "date": self.date
        }