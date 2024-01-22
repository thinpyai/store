"""
Exception Module.
"""
from http import HTTPStatus


class SystemException(Exception):
    """
    System exception

    Args:
        Exception (class): System exception
    """

    def __init__(self, message: str, error_type: str = 'SystemException',
                 status_code: tuple = HTTPStatus.BAD_REQUEST) -> None:
        """Initialize the system exception.

        Args:
            message (str): Error message
            error_type (str, optional): Error type. Defaults to 'SystemException'.
            status_code (tuple, optional): Error http status code. Defaults to HTTPStatus.BAD_REQUEST.
        """
        self.error_type = error_type
        self.status_code = status_code
        self.message = message

    def _generate_message(self, base: str, param: dict):
        if not param:
            message = base
        else:
            message = base + ' : ' + \
                ', '.join([f'{k}={v}' for k, v in param.items()])
        return message


class DataNotFound(SystemException):
    """
    Data not found class

    Args:
        SystemException (class): System exception
    """

    def __init__(self, key_params: dict = None):
        """
        Inititalize data not found exception.

        Args:
            key_params (dict, optional): Expected key parameters . Defaults to None.
        """
        message = self._generate_message('Data was not found.', key_params)
        super().__init__(message, self.__class__.__name__, HTTPStatus.NOT_FOUND)


class DataAlreadyExist(SystemException):
    """
    Data already exist class

    Args:
        SystemException (class): System exception
    """

    def __init__(self, key_params: dict = None):
        """
        Inititalize data not found exception.

        Args:
            key_params (dict, optional): Expected key parameters . Defaults to None.
        """
        message = self._generate_message('Data is already existed.', key_params)
        super().__init__(message, self.__class__.__name__, HTTPStatus.NOT_FOUND)
