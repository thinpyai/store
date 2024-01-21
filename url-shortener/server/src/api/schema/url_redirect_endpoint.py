"""Endpoints modules."""

from fastapi import Depends
from fastapi.responses import RedirectResponse
from fastapi.routing import APIRouter

from context import get_url_service
from domain.service.url_service import UrlService
from setting import settings

router = APIRouter(prefix=f'/{settings.service_name}',
                   tags=['redirect-to-original'])


@router.get("/{short_code}", response_class=RedirectResponse, status_code=302)
async def redirect_original_url(short_code: str, url_service: UrlService = Depends(get_url_service)):
    """
    Redirect to original url.

    Args:
        short_code (str): Shortened code
        url_service (UrlService, optional): Url service. Defaults to Depends(get_url_service).

    Returns:
        RedirectResponse: Redirect response to original url
    """
    original_url = url_service.retrieve_original_url(short_code)
    return original_url
