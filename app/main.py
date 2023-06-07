from fastapi import FastAPI

from .books_api import setup_books_api
from .configs.database import setup_database

app = FastAPI()

setup_database(app)
setup_books_api(app)
