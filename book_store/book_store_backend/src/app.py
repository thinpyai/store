"""
Main file to start running the server

Author: Thin Pyai Win
Date:  27 August 2023
"""
import logging
from logging import CRITICAL, DEBUG, ERROR, INFO, WARN

from api import api
from router import book_app

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

    api.include_router(book_app, prefix='/graphql/book')
    return api
