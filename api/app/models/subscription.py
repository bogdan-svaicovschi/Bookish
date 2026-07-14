from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime

from app.helpers.database import Base
from app.models.user import User


class Subscription(Base):
    __tablename__ = "Subscription"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    start_date = Column(datetime)
    end_date = Column(datetime)
    name = Column(String)
    discount = Column(float)
    user = Column(Integer, ForeignKey("User.id"))


    def __init__(self, name, start_date, end_date, discount, user):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.discount = discount
        self.user = user

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "discount": self.discount,
            "user": self.user
        }