"""
URL data types
"""

import strawberry


@strawberry.type
class ShortenedUrlOutput():
    """Book schema object type"""
    shortened_url: str
    long_url: str
