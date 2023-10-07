"""
Setting file to setup constant values

Author: Thin Pyai Win
Date:  7 October 2023
"""

import logging
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """System setting.

    Args:
        BaseSettings (class): System base settings
    """
    root_path = Path(__file__).parent.parent
    config_file_name = '.env.dev'
    config_file_path = f'{root_path}/conf/{config_file_name}'
    model_config = SettingsConfigDict(env_file=config_file_path)


@lru_cache()
def get_settings():
    """Get system settings.

    Returns:
        Settings: System setting
    """
    return Settings()


settings = get_settings()
