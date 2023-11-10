from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Type

from data import models, schemas
from data.database import engine
from data.get_db import get_db
from services import movie_service

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix='/api/movies', tags=['movies'])


@router.get('/', response_model=list[schemas.Movie], status_code=status.HTTP_200_OK)
def get_movies(db: Session = Depends(get_db)) -> list[Type[schemas.Movie]]:
    movies = movie_service.get_movies(db)
    return movies  # type: ignore


@router.get('/{movie_id}', response_model=schemas.Movie, status_code=status.HTTP_200_OK)
def get_movie_by_id(movie_id: int, db: Session = Depends(get_db)) -> Type[schemas.Movie]:
    movie = movie_service.get_movie_by_id(movie_id, db)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')
    return movie  # type: ignore


@router.post('/', response_model=schemas.Movie, status_code=status.HTTP_201_CREATED)
def add_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)) -> schemas.Movie:
    created_movie = movie_service.add_movie(movie, db)
    return created_movie


@router.delete('/{movie_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    try:
        movie_service.delete_movie(movie_id, db)
        return status.HTTP_204_NO_CONTENT
    except IndexError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found') from err
