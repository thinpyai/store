"""Url service module.

Returns:
    UrlService: Url service
"""
import hashlib

from infra.repository.url_repository import UrlRepository

DOMAIN_VALUE = "localhost:8080"
PROTOCOL = "http"
SERVICE_CODE = "shorten-url"


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
        short_url = f"{PROTOCOL}://{DOMAIN_VALUE}/{SERVICE_CODE}/{short_code}"
        # TODO check same short_code in db before storing
        self.__url_repository.create_url_record(original_url, short_url, short_code)
        # TODO output log
        return short_url

    def retrieve_original_url(self, short_code) -> str:
        """_summary_

        Args:
            short_code (_type_): _description_

        Returns:
            str: _description_
        """
        url = self.__url_repository.get_url_record(short_code)
        if not url:
            # TODO raise error
            pass
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
