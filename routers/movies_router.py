from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from data import models, schemas
from data.database import engine
from data.get_db import get_db
from services import movie_service

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix='/api/movies', tags=['movies'])


@router.get('/', response_model=list[schemas.Movie], status_code=status.HTTP_200_OK)
def get_movies(db: Session = Depends(get_db)) -> list[schemas.Movie]:
    return movie_service.get_movies(db)


@router.get('/{movie_id}', response_model=schemas.Movie, status_code=status.HTTP_200_OK)
def get_movie_by_id(movie_id: int, db: Session = Depends(get_db)) -> schemas.Movie:
    movie = movie_service.get_movie_by_id(movie_id, db)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')
    return movie


@router.post('/', response_model=schemas.Movie, status_code=status.HTTP_201_CREATED)
def add_movie(movie: schemas.Movie, db: Session = Depends(get_db)) -> schemas.Movie:
    return movie_service.add_movie(movie, db)


@router.delete('/{movie_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, db: Session = Depends(get_db)) -> None:
    try:
        movie_service.delete_movie(movie_id, db)
    except IndexError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found') from err
