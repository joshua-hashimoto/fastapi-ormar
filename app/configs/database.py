from databases import Database
from fastapi import FastAPI
from sqlalchemy import MetaData

from .settings import get_settings

settings = get_settings()

def get_db_url():
    return settings.db_url


database = Database(get_db_url())
metadata = MetaData()

def setup_database(app: FastAPI):
    app.state.database = database

    @app.on_event("startup")
    async def startup() -> None:
        database_ = app.state.database
        if not database_.is_connected:
            await database_.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        database_ = app.state.database
        if database_.is_connected:
            await database_.disconnect()
