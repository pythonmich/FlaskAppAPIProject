import os

from utils.config import load_config

basedir = os.path.abspath(os.path.dirname(__file__))
PATH = "C:/Users/Hewlette-Packard/Desktop/pycham Projects/FlaskAPP/app.env"
_SECRET_KEY = load_config(PATH, "TOKEN", "SECRET_KEY")


class BaseConfig:
    SECRET_KEY = _SECRET_KEY
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = load_config(PATH, "DATABASE", "DB_SOURCE")


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = load_config(PATH, "DATABASE", "DB_TEST")
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    SECRET_KEY = _SECRET_KEY
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = load_config(PATH, "DATABASE", "DB_SOURCE")
