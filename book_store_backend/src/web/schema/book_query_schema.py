"""Book query schema file."""

from typing import Optional

import strawberry
from strawberry.types import Info

from web.type.book_type import BookDetailType, BookListType


def get_book_service(info: Info):
    """Get book service.

    Args:
        info (Info): FastAPI info data context

    Returns:
        BookService: Book service object
    """
    return info.context.book_service

@strawberry.type(name='BookQuery')
class Query:
    """ Book Query """

    @strawberry.field
    def list_book(self, info: Info) -> BookListType:
        """List books.

        Args:
            info (Info): FastAPI info data context

        Returns:
            BookListType: Book information object list
        """
        books = get_book_service(info).list_books()
        return BookListType(books=books)

    @strawberry.field
    def get_book(self, info: Info, book_id: str) -> Optional[BookDetailType]:
        """Get book by id.

        Args:
            info (Info): FastAPI info data context
            book_id (str): Book ID

        Returns:
            Optional[BookDetailType]: Book information object or None
        """
        book = get_book_service(info).get_book(book_id)
        return book
