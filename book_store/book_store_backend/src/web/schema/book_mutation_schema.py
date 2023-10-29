"""Book mutation schema file."""

import strawberry
from strawberry.types import Info

from domain.model.book import Book
from web.type.book_type import BookDetailInput, BookType


def get_book_service(info: Info):
    """Get book service.

    Args:
        info (Info): FastAPI info data context

    Returns:
        BookService: Book service object
    """
    return info.context.book_service

@strawberry.type(name='BookMutation')
class Mutation:
    """ Book Mutation class """

    @strawberry.field
    def register_book(self, info: Info, book_input: BookDetailInput) -> BookType:
        """Register new book.

        Args:
            info (Info): FastAPI info data context
            book_input (BookDetailInput): Book information detail to register

        Returns:
            BookType: Resulted book information object
        """
        book = Book(**book_input.__dict__)
        registered_book = get_book_service(info).register_book(book)
        return registered_book

    @strawberry.field
    def edit_book(self, info: Info, book_input: BookDetailInput) -> BookType:
        """Edit book.

        Args:
            info (Info): FastAPI info data context
            book_input (BookDetailInput): Book information detail to edit.

        Returns:
            BookType: Resulted book information object
        """
        book = Book(**book_input.__dict__)
        edited_book = get_book_service(info).edit_book(book)
        return edited_book

    @strawberry.field
    def delete_book(self, info: Info, book_id: str) -> BookType:
        """Delete book by id.

        Args:
            info (Info): FastAPI info data context
            book_id (str): Book ID

        Returns:
            BookType: Resulted book information object
        """
        deleted_book = get_book_service(info).delete_book(book_id)
        return deleted_book
