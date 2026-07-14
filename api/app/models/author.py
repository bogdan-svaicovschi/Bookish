from sqlalchemy import Column, Integer, String

from app.helpers.database import Base

class Author(Base):
    __tablename__ = "Author"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
    