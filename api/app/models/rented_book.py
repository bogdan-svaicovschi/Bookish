from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime

from app.helpers.database import Base
from app.models.order import Order


class RentedBook(Base):
    __tablename__ = "RentedBook"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date_rented = Column(datetime)
    due_date = Column(datetime)
    order = Column(Integer, ForeignKey("Order.id"))


    def __init__(self, date_rented, due_date, order):
        self.date_rented = date_rented
        self.due_date = due_date
        self.order = order

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "date_rented": self.date_rented,
            "due_date": self.due_date,
            "order": self.order
        }