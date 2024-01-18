import os

from infra.table.book_table import mapper_registry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseContext:
    def initialize_db(self):
        db_type = 'sqlite'
        db_dir = 'db'
        db_interface = 'sqlite'
        db_name = "url_service"
        db_url = f'{db_interface}:///../{db_dir}/{db_name}.db?check_same_thread=False'

        # TODO get the current directory from file path

        if db_type == "sqlite" and not os.path.exists(f'../{db_dir}'):
            os.mkdir(f'../{db_dir}')

        engine = create_engine(db_url)

        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        Base = mapper_registry.generate_base()
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
