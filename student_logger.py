import logging
from functools import wraps


FORMAT = '{levelname:<5} - {asctime} сообщение: {msg}'
logging.basicConfig(format=FORMAT, filename='student.log',
                    encoding='utf-8', style='{', level=logging.NOTSET)


def log_decorator(func):
    logger = logging.getLogger(__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            logger.debug(f'{args[0].__class__.__name__}.{func.__name__} {args} {kwargs} {res}')
            return res
        except Exception as err:
            logging.exception(err)

    return wrapper


def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)) and not attr.startswith('_') or attr == '__init__':
            # if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
