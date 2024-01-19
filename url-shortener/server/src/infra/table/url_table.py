import uuid
from datetime import timezone

from sqlalchemy import Boolean, Column, DateTime, String, Table
from sqlalchemy.orm import registry
from sqlalchemy.sql import func

from domain.model.url import Url
from infra.table.type import GUID

mapper_registry = registry()

url = Table(
    'urls',
    mapper_registry.metadata,
    Column('id', GUID(), primary_key=True, default=uuid.uuid4),
    Column('short_url', String(128), nullable=False),
    Column('long_url', String(128), nullable=True),
    Column('is_valid', Boolean, default=False),
    Column('created_at', DateTime(timezone=True), server_default=func.now(tz=timezone.utc)),
    Column('updated_at', DateTime(timezone=True), onupdate=func.now(tz=timezone.utc)),
)
mapper_registry.map_imperatively(Url, url)
