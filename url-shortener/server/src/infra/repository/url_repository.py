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
    def store_url_record(self, long_url: str, short_url: str) -> Url:
        url = Url(short_url=short_url, long_url=long_url, is_valid=True)
        self.db.add(url)
        return url
