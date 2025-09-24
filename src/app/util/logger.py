import functools
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("custom_logger")

def enable_logs(func):
    """
    Decorator that logs when a function is executed and what it returns.
    Args:
        func: The function to be decorated
    Usage:
        @enable_logs
        def my_func(...):
            ...
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if os.getenv("ENABLE_LOGS").lower() == 'true':
            logger.info(f"START: {func.__module__}.{func.__name__}")
            result = func(*args, **kwargs)
            logger.info(f"END: {func.__module__}.{func.__name__} | RETURNED: {result}")
        else:
            result = func(*args, **kwargs)
        return result

    return wrapper
