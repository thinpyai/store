"""
Book store system exception

Author: Thin Pyai Win
Date:  27 August 2023
"""
from http import HTTPStatus


class BookStoreException(Exception):
    """
    Book store server general exception.

    Args:
        Exception: _description_
    """
    pass


class ServiceUnavailableError(BookStoreException):
    """Exception when requested service is not available/ implemented.

    Args:
        BookStoreException: Book store server exception
    """

    def __init__(self, message, params):
        message = self._generate_message(message, params)
        super().__init__('ServiceUnavailableError', HTTPStatus.INTERNAL_SERVER_ERROR)

    def _generate_message(self, base: str, param: dict):
        if not param:
            message = base
        else:
            message = base + ' : ' + \
                ', '.join([f'{k}={v}' for k, v in param.items()])
        return message
