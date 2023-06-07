from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


class Settings(BaseSettings):
    base_dir: Path = BASE_DIR
    db_url = f"sqlite:///{BASE_DIR!s}/db/dev.sqlite"


@lru_cache
def get_settings():
    return Settings()
