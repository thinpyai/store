"""
Book store application exception

Author: Thin Pyai Win
Date:  27 August 2023
"""

from http import HTTPStatus

from system_exception import BookStoreException


class BookStoreAppException(BookStoreException):
    """Exception when book store application has error

    Args:
        BookStoreException (Exception): System exception
    """

    def __init__(self, message, error_type='BookStoreAppException', http_status_code=HTTPStatus.BAD_REQUEST):
        self.message = message
        self.http_status_code = http_status_code
        self.error_type = error_type

    def _generate_message(self, base: str, param: dict):
        if not param:
            message = base
        else:
            message = base + ' : ' + \
                ', '.join([f'{k}={v}' for k, v in param.items()])
        return message
