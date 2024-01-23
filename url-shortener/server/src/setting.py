"""
Setting module.

Returns:
    Settings: FastAPI base setting
"""

import logging
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """System setting.

    Args:
        BaseSettings (class): System base settings
    """
    service_name: str = ""
    domain_value: str = ""
    protocol: str = ""
    db_type: str = ""
    db_interface: str = ""
    db_dir: str = ""

    class Config:
        """
        Import configuration from config file.
        """
        root_path = Path(__file__).parent.parent
        config_dir = 'conf'
        config_file_name = '.env'
        env_file = f'{root_path}/{config_dir}/{config_file_name}'


@lru_cache()
def get_settings():
    """Get system settings.

    Returns:
        Settings: System setting
    """
    return Settings()


settings = get_settings()
