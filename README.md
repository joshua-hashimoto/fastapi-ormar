# FastAPI + ormar

- [FastAPI + ormar](#fastapi--ormar)
  - [Summary](#summary)
  - [Tech Stack](#tech-stack)
  - [Local development setup](#local-development-setup)
    - [.env](#env)
    - [Database migration](#database-migration)
      - [Step1: Initiate alembic(only once)](#step1-initiate-alembiconly-once)
      - [Step2: Set metadata and models](#step2-set-metadata-and-models)
      - [Step3: Set DB url](#step3-set-db-url)
      - [Step4: (Auto) Generate migration files](#step4-auto-generate-migration-files)
      - [Step5: check for ormar imports](#step5-check-for-ormar-imports)
      - [Step6: Apply migrations](#step6-apply-migrations)
    - [Start FastAPI](#start-fastapi)
    - [Switching to Test Database](#switching-to-test-database)
  - [Deployment](#deployment)
  - [Contributrs](#contributrs)

## Summary

A demonstration application using FastAPI and ormar.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com)
- [ormar](https://collerek.github.io/ormar/)

## Local development setup

### .env

```sh
ENVIRONMENT=develop
```

### Database migration

When using ormar, we need to make migration files by ourselves.
For this we use **[alembic](https://github.com/alembic/alembic)**.

#### Step1: Initiate alembic(only once)

```sh
alembic init migrations
```

`migrations` is a name of the folder. This can be anything.

#### Step2: Set metadata and models

When making a migration for your models, you need to **import** the models into `env.py` created by alembic and set the metadata to `target_metadata`.

```py
# in migrations/env.py
from .models import Book
from .database import metadata

target_metadata = metadata
```

#### Step3: Set DB url

Usually you would need to set the `sqlalchemy.url` in your alembic file. But in order to make this connection more dynamic, we set this value in `env.py` as follows.

```py
# in migrations/env.py
from .database import get_db_url

target_metadata = metadata
config.set_main_option("sqlalchemy.url", get_db_url())
```

#### Step4: (Auto) Generate migration files

```sh
alembic revision --autogenerate -m "<write migration comments>"
```

#### Step5: check for ormar imports

After Step4, checked the auto generated migration file.
If you see `ormar` in the file, please import the `ormar` package inside the file.
If you skip this step, Step6 will fail.

#### Step6: Apply migrations

```sh
alembic upgrade head
```

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

### Switching to Test Database

If you want to use a different database for running unit tests, change the value of environment variable ENVIRONMENT to `test`

```py
from .settings import settings


TEST_DB_URL = f"sqlite:///{str(settings.base_dir)}/db/test_db.sqlite"
DB_URL = f"sqlite:///{str(settings.base_dir)}/db/dev_db.sqlite"
# DB_URL = f"postgresql://root:root1234@db:5432/dev_db" # your DB url


def get_db_url():
    if settings.environment == "test":
        return TEST_DB_URL
    return DB_URL
```

## Deployment

Not deployed.

## Contributrs

- [Joshua Hashimoto](https://github.com/joshua-hashimoto?tab=repositories)
