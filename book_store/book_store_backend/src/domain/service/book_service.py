
from typing import List

from domain.model.book import Book
from infra.repository.book_repository import BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository) -> None:
        self.__book_repository = book_repository

    def list_books(self) -> List[Book]:
        books = self.__book_repository.find_books()
        return books

    def get_book(self, book_id: str):
        book = self.__book_repository.find_book(book_id)
        return book

    def register_book(self, book: Book) -> Book:
        result = self.__book_repository.create_book(book)
        return result

    def edit_book(self, book: Book):
        result = self.__book_repository.update_book(book)
        return result

    def delete_book(self, book_id: str):
        result = self.__book_repository.delete_book(book_id)
        return result
