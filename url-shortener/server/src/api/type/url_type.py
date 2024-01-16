"""
URL data types
"""

import strawberry


@strawberry.type
class ShortenedUrlOutput():
    """Book schema object type"""
    url: str


@strawberry.input
class LongUrlInput():
    """Book detail input schema object type"""
    url: str
