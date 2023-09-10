import logging
from functools import lru_cache

from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    pass


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
