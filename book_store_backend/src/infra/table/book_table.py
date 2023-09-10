import uuid
from datetime import timezone

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Table
from sqlalchemy.orm import registry
from sqlalchemy.sql import func

from domain.model.book import Book
from infra.table.type import GUID

mapper_registry = registry()

book = Table(
    'books',
    mapper_registry.metadata,
    Column('id', GUID(), primary_key=True, default=uuid.uuid4),
    Column('name', String(128), nullable=False),
    Column('author', String(128), nullable=True),
    Column('price', Float, nullable=True),
    Column('edition_no', Integer, nullable=True),
    Column('brief', String(128), nullable=True),
    Column('is_valid', Boolean, default=False),
    Column('author_intro', String(128), nullable=True),
    Column('published_date', DateTime(timezone=True), nullable=True),
    Column('created_at', DateTime(timezone=True), server_default=func.now(tz=timezone.utc)),
    Column('updated_at', DateTime(timezone=True), onupdate=func.now(tz=timezone.utc)),
)
mapper_registry.map_imperatively(Book, book)
