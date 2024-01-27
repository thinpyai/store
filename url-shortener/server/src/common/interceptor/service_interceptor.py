"""
Interceptor module.

Returns:
    wrapper: Wrapper for database transaction decorator
"""
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def transactional(func):
    """
    Database transaction decorator for service layer.
    Target function must have db field.
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper for database commit connection.

        Returns:
            func: Commit function
        """
        result = func(self, *args, **kwargs)

        if hasattr(self, 'db'):
            try:
                self.db.commit()
                logger.debug('Transaction is committed.')
            except BaseException:
                self.db.rollback()
                logger.debug('Transaction is rollbacked.')
                raise
        else:
            logger.debug('This instance has no `db` field.')

        return result

    return wrapper
