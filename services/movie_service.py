from sqlalchemy.orm import Session

from data import models, schemas


def get_movies(db: Session) -> list[models.Movie]:
    return db.query(models.Movie).all()  # type: ignore


def get_movie_by_id(movie_id: int, db: Session) -> models.Movie | None:
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()  # type: ignore


def add_movie(movie: schemas.Movie, db: Session) -> models.Movie:
    db_movie = models.Movie(
        title=movie.title,
        description=movie.description,
        genre=movie.genre,
        rating=movie.rating,
        release_date=movie.release_date
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie(movie_id: int, db: Session) -> None:
    db_movie = get_movie_by_id(movie_id, db)
    if db_movie is None:
        raise IndexError('The specified movie could not be found.')
    db.delete(db_movie)
    db.commit()
