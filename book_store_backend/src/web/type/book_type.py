from typing import List, Optional

import strawberry


@strawberry.type
class BookType():
    name: str
    author: str
    published_date: str
    price: float
    id: str


@strawberry.type
class BookDetailType(BookType):
    edition_no: int = 1
    brief: Optional[str] = None
    author_intro: Optional[str] = None


@strawberry.type
class BookListType():
    books: List[BookType] = None


@strawberry.input
class BookDetailInput(BookDetailType):
    id: str = None
