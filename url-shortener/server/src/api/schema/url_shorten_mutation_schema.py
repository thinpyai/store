"""Mutation schema file."""

import strawberry
from strawberry.types import Info

# from domain.model.book import Book
from api.type.url_type import ShortenedUrlOutput, LongUrlInput


@strawberry.type(name='UrlShortenMutation')
class Mutation:
    """ URl shorten mutation class """

    @strawberry.field
    def shorten_url(self, info: Info, 
                    longUrlInput: LongUrlInput) -> ShortenedUrlOutput:
        """Generate a shortened url

        Args:
            info (Info): FastAPI info data context

        Returns:
            BookType: Resulted book information object
        """
        return None
