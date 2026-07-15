from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime

from app.helpers.database import Base
from app.models.subscription import Subscription
from app.models.rented_book import RentedBook


class Penalty(Base):
    __tablename__ = "Penalty"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    percentage = Column(Integer)
    value = Column(Integer)
    subscription = Column(Integer, ForeignKey("Subscription.id"))
    book = Column(Integer, ForeignKey("RentedBook.id"))


    def __init__(self, percentage, value, subscription, book):
        self.percentage = percentage
        self.book = book
        self.subscription = subscription
        self.value = value

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "percentage": self.percentage,
            "book": self.book,
            "subscription": self.subscription,
            "value": self.value
        }
    