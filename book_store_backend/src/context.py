from fastapi import Depends
from strawberry.fastapi import BaseContext

from database import get_db
from domain.service.book_service import BookService
from infra.repository.book_repository import BookRepository


def get_book_repository(db=Depends(get_db)):
    return BookRepository(db)


def get_book_service(book_repository: BookRepository = Depends(get_book_repository)):
    return BookService(
        book_repository=book_repository)


class BookContext(BaseContext):
    def __init__(self, book_service: BookService):
        self.book_service: BookService = book_service


async def get_book_context(
        book_service: BookService = Depends(get_book_service)
) -> BookContext:
    return BookContext(
        book_service=book_service
    )
