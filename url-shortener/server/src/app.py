"""
Main file to start running the server

Author: Thin Pyai Win
"""
import logging
from logging import CRITICAL, DEBUG, ERROR, INFO, WARN

from api.api import api
from router import url_shortener_app

logger = logging.getLogger(__name__)

log_level = {
    'critical': CRITICAL,
    'error': ERROR,
    'warn': WARN,
    'info': INFO,
    'debug': DEBUG
}

logger = logging.getLogger(__name__)


def main():

    api.include_router(url_shortener_app, prefix='/service/url-shortener')
    return api
