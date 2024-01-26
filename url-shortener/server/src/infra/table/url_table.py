"""
Table and data class mapper registry module
"""

import uuid
from datetime import timezone

from sqlalchemy import Boolean, Column, DateTime, String, Table
from sqlalchemy.orm import registry
from sqlalchemy.sql import func

from domain.model.url import Url
from infra.table.type import GUID

table_registry = registry()

url = Table(
    'urls',
    table_registry.metadata,
    Column('id', GUID(), primary_key=True, default=uuid.uuid4),
    Column('short_url', String(128), nullable=False),
    Column('original_url', String(128), nullable=False),
    Column('short_code', String(128), nullable=False, primary_key=True),
    Column('is_valid', Boolean, default=False),
    Column('created_at', DateTime(timezone=True), server_default=func.now(tz=timezone.utc)),
    Column('updated_at', DateTime(timezone=True), onupdate=func.now(tz=timezone.utc))
)
table_registry.map_imperatively(Url, url)
