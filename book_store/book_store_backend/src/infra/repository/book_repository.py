from typing import List

from sqlalchemy.orm import Session

from common.interceptor.service_interceptor import transactional
from domain.model.book import Book


class BookRepository:

    def __init__(self, db: Session) -> None:
        self.db = db

    def find_books(self, is_valid: bool = True) -> List[Book]:
        books = self.db.query(Book).filter(Book.is_valid == is_valid).all()
        return books

    def find_book(self, book_id: str) -> Book:
        book = self.db.query(Book).get(book_id)
        return book

    @transactional
    def create_book(self, book: Book) -> Book:
        result = self.db.add(book)
        return result

    @transactional
    def update_book(self, book: Book) -> Book:
        return book

    @transactional
    def delete_book(self, book_id: str):
        result = self.db.query(Book).filter(Book.id == book_id).delete(synchronize_session=False)
        return result
