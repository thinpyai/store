"""Mutation schema file."""

import strawberry
from strawberry.types import Info

from api.type.url_type import ShortenedUrlOutput


def get_url_service(info: Info):
    """Get Url service class object.

    Args:
        info (Info): FastAPI info data context

    Returns:
        UrlService: Url service object
    """
    return info.context.url_service


@strawberry.type(name='UrlShortenMutation')
class Mutation:
    """ URl shorten mutation class """

    @strawberry.field
    def shorten_url(self, info: Info, long_url: str) -> ShortenedUrlOutput:
        """Generate a shortened url

        Args:
            info (Info): FastAPI info data context

        Returns:
            BookType: Resulted book information object
        """
        url_service = get_url_service(info=info)
        short_url = url_service.shorten_url(long_url)
        return ShortenedUrlOutput(short_url == short_url, long_url=long_url)
