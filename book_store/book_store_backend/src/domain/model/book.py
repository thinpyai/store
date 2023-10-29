from dataclasses import dataclass


@dataclass
class Book:
    name: str
    author: str
    published_date: str
    price: float
    edition_no: int = 1
    id: str = None
    brief: str = None
    author_intro: str = None
    is_valid: bool = False
