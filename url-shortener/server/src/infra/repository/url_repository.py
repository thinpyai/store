"""
Url repository module.

Returns:
    UrlRepository: Url repository
"""

from sqlalchemy.orm import Session

from common.interceptor.service_interceptor import transactional
from domain.model.url import Url


class UrlRepository:
    """
    Url repository to deal with url table in database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    @transactional
    def create_url_record(self, long_url: str, short_url: str, short_code: str) -> Url:
        """
        Create url record.

        Args:
            long_url (str): Original url
            short_url (str): Shortened url
            short_code (str): Short code

        Returns:
            Url: Stored url record
        """
        url = Url(short_url=short_url, long_url=long_url, short_code=short_code, is_valid=True)
        self.db.add(url)
        return url

    def get_url_record(self, short_code: str) -> Url:
        """
        Get url record

        Args:
            short_code (str): Shortened url

        Returns:
            Url: Stored url record
        """
        url = self.db.query(Url).filter(Url.short_code == short_code).first()
        return url
