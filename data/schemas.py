from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    genre: str
    rating: float
    release_date: date

    model_config = ConfigDict(from_attributes=True)
