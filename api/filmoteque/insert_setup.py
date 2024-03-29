from sqlalchemy import insert
import csv
from .models.user import UserModel
from .models.movie import MovieModel, movies_genres
from .models.director import DirectorModel
from .models.genre import GenreModel
from .models.role import RoleModel
from .database.insertion_data import genre_names, directors, users, roles
from .db import db


def insert_roles():
    db.session.execute(insert(RoleModel), roles)
    db.session.commit()


def insert_users():
    db.session.execute(
        insert(UserModel),
        users,
    )
    db.session.commit()


def insert_genres():
    db.session.execute(
        insert(GenreModel),
        [{"name": g} for g in genre_names],
    )
    db.session.commit()


def insert_directors():
    db.session.execute(
        insert(DirectorModel),
        [{"name": d} for d in directors],
    )
    db.session.commit()


def insert_movies():
    with open("filmoteque/database/movies.csv") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        header = next(reader)
        for i in reader:
            kwargs = {column: value for column, value in zip(header, i)}
            new_entry = MovieModel(**kwargs)
            db.session.add(new_entry)
        db.session.commit()


def insert_movies_genres():
    with open("filmoteque/database/movies-genres_data.csv") as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)
        for i in reader:
            kwargs = {column: value for column, value in zip(header, i)}
            db.session.execute(insert(movies_genres).values(kwargs))
        db.session.commit()

    db.session.commit()


def insert_all():
    insert_roles()
    insert_users()
    insert_genres()
    insert_directors()
    insert_movies()
    insert_movies_genres()
