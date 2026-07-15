from pydantic import BaseModel

class BookCreate(BaseModel):
    name: str
    genre: int
    