from datetime import date
from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: str
    genre: str
    rating: float
    release_date: date


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True
