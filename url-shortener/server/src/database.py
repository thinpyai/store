"""
Database connection setting module.

Yields:
    DatabaseContext: Database connection context
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infra.table.url_table import table_registry
from setting import settings

DB_NAME = 'url_service'


class DatabaseContext:
    """
    Database context class
    """

    def initialize_db(self):
        """
        Initialize database engine.
        """
        db_url = f'{settings.db_interface}:///../{settings.db_dir}/{DB_NAME}.db?check_same_thread=False'

        if settings.db_type == "sqlite" and not os.path.exists(f'../{settings.db_dir}'):
            os.mkdir(f'../{settings.db_dir}')

        engine = create_engine(db_url)

        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        Base = table_registry.generate_base()
        Base.metadata.create_all(bind=engine)


database_context = DatabaseContext()
database_context.initialize_db()


def get_db():
    """
    Get database

    Yields:
        SessionLocal: Local session for database connection
    """
    db = database_context.SessionLocal()
    try:
        yield db
    finally:
        db.close()
