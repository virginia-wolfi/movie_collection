class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_MASK_SWAGGER = False
    SECRET_KEY = "20d59e04e26833e150ee3da1ea0f175905685e91"


class DevelopmentConfig(Config):
    # create database in Postgres and insert
    # your database URI for development config
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://postgres:psw@localhost/film_collection"
    )


class TestingConfig(Config):
    # create database in Postgres and
    # insert your database URI for testing config
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://postgres:psw@localhost/film_collection_test"
    )
    TESTING = True
