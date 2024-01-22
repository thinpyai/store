"""
Url service module.

Returns:
    UrlService: Url service
"""
import hashlib
import logging
from dataclasses import asdict

from exception.app_exception import DataAlreadyExist, DataNotFound
from infra.repository.url_repository import UrlRepository
from setting import settings

logger = logging.getLogger(__name__)


class UrlService:
    """
    Url service class
    """

    def __init__(self, url_repository: UrlRepository) -> None:
        """
        Initialization
        """
        self.__url_repository = url_repository

    def shorten_url(self, original_url: str) -> str:
        """
        Shorten url

        Args:
            original_url (str): Orignal url

        Returns:
            str: Shortened url
        """
        short_code = self.__generate_shortened_code(original_url)
        existing_url = self.__url_repository.get_url_record(short_code)

        if existing_url:
            error_key_params = asdict(existing_url)
            logger.error('Fail to create short url.: existing_url=%s', str(error_key_params))
            raise DataAlreadyExist(error_key_params)

        short_url = f"{settings.protocol}://{settings.domain_value}/{settings.service_name}/{short_code}"
        self.__url_repository.create_url_record(original_url, short_url, short_code)
        logger.info('Short url is successfully created.: short_url=%s', short_url)

        return short_url

    def retrieve_original_url(self, short_code: str) -> str:
        """Retrieve original url by short_code

        Args:
            short_code (str): _description_

        Returns:
            str: _description_
        """
        url = self.__url_repository.get_url_record(short_code)

        if not url:
            logger.error('Fail to retrieve short url.: short_code=%s', short_code)
            raise DataNotFound({'short_code': short_code})

        return url.original_url

    def __generate_shortened_code(self, original_url: str) -> str:
        """
        Generate shortened code from original url.

        Args:
            original_url (str): Orignal url

        Returns:
            str: Shortened code
        """
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(original_url.encode())
        hash_value = hash_algorithm.hexdigest()
        short_code = hash_value[:16]
        return short_code
