"""Url service module.

Returns:
    UrlService: Url service
"""
import hashlib
from dataclasses import asdict

from exception.app_exception import DataAlreadyExist, DataNotFound
from infra.repository.url_repository import UrlRepository
from setting import settings


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
            # TODO log output
            error_key_params = asdict(existing_url)
            raise DataAlreadyExist(error_key_params)

        short_url = f"{settings.protocol}://{settings.domain_value}/{settings.service_name}/{short_code}"

        self.__url_repository.create_url_record(original_url, short_url, short_code)
        # TODO output log
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
            # log output
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
