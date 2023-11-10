from sqlalchemy import Column, Date, Float, Integer, String

from data.database import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    genre = Column(String(50))
    rating = Column(Float)
    release_date = Column(Date)
