"""
URL data types
"""

import strawberry


@strawberry.type
class ShortenedUrlOutput():
    """Book schema object type"""
    short_url: str
    long_url: str
