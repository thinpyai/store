"""
Context module.
This module provide contexts of the system.

Returns:
    UrlContext: Url context which can access to url services.
"""
from fastapi import Depends
from strawberry.fastapi import BaseContext
from domain.service.url_service import UrlService


class UrlContext(BaseContext):
    """UrlContext BaseContext

    Args:
        BaseContext (_type_): _description_
    """
    def __init__(self, url_service: UrlService):
        self.url_service: UrlService = url_service


def get_url_service():
    """Get url service class object.

    Returns:
        UrlService: UrlService class object
    """
    return UrlService()


async def get_url_context(
        url_service: UrlService = Depends(get_url_service)) -> UrlContext:
    """Get UrlContext class object.

    Args:
        url_service (UrlService, optional): UrlService class object. Defaults to Depends(get_url_service).

    Returns:
        UrlContext: UrlContext class object
    """
    return UrlContext(url_service=url_service)