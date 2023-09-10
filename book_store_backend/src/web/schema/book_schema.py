from typing import Optional

import strawberry
from strawberry.types import Info

from common.util.type_converter import TypeConverter
from domain.model.book import Book
from domain.service.book_service import BookService
from web.type.book_type import (BookDetailInput, BookDetailType, BookListType,
                                BookType)


def get_book_service(info: Info) -> BookService:
    return info.context.book


@strawberry.type(name='BookQuery')
class Query:

    @strawberry.field
    def list_book(self, info: Info) -> BookListType:
        books = get_book_service(info).list_books()
        return BookListType(books=books)

    @strawberry.field
    def get_book(self, info: Info, book_id: str) -> Optional[BookDetailType]:
        book = get_book_service(info).get_book(book_id)
        return book


@strawberry.type(name='BookMutation')
class Mutation:

    @strawberry.field
    def register_book(self, info: Info, book_input: BookDetailInput) -> BookType:
        # book_dict = TypeConverter.convert_to_dict(book, [BookDetailInput])
        book = Book(**book_input.__dict__)
        registered_book = get_book_service(info).register_book(book)
        return registered_book

    @strawberry.field
    def edit_book(self, info: Info, book_input: BookDetailInput) -> BookType:
        # book_dict = TypeConverter.convert_to_dict(book, [BookDetailInput])
        book = Book(**book_input.__dict__)
        edited_book = get_book_service(info).edit_book(book)
        return edited_book

    @strawberry.field
    def delete_book(self, info: Info, book_id: str) -> BookType:
        deleted_book = get_book_service(info).delete_book(book_id)
        return deleted_book
