from fastapi import FastAPI

from .routers import setup_routers


def setup_books_api(app: FastAPI):
    setup_routers(app)
