"""Book query schema file."""

from typing import Optional

import strawberry
from strawberry.types import Info
from web.type.book_type import (BookDetailType, BookListType)


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
        books = info.context.book.list_books()
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
        book = info.context.book.get_book(book_id)
        return book
