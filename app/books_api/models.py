import uuid
from datetime import datetime

import ormar

from app.configs.database import database, metadata


class Book(ormar.Model):
    pk: int = ormar.Integer(primary_key=True)
    id: uuid.UUID = ormar.UUID(default=uuid.uuid4)
    title: str = ormar.String(max_length=150)
    description: str = ormar.Text(nullable=True)
    price: int = ormar.Integer()
    unit: str = ormar.String(max_length=3)
    created_at: datetime = ormar.DateTime(default=datetime.now)
    updated_at: datetime = ormar.DateTime(default=datetime.now)
    is_active: bool = ormar.Boolean(default=True)

    class Meta(ormar.ModelMeta):
        metadata = metadata
        database = database
        tablename = "books"
