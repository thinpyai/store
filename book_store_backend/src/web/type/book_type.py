from typing import List, Optional

import strawberry


@strawberry.type
class BookType():
    """Book schema object type"""
    name: str
    author: str
    published_date: str
    price: float
    id: str


@strawberry.type
class BookDetailType(BookType):
    """Book detail schema object type"""
    edition_no: int = 1
    brief: Optional[str] = None
    author_intro: Optional[str] = None


@strawberry.type
class BookListType():
    """Book list schema object type"""
    books: List[BookType] = None


@strawberry.input
class BookDetailInput(BookDetailType):
    """Book detail input schema object type"""
    id: str = None
