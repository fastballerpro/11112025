import datetime
from functools import wraps

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        elapsed = (end - start).total_seconds()

        print(f"{func.__name__} took {elapsed:.3f} seconds")
        return result
    return wrapper


def round_result(ndigits: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, (int, float)):
                return round(result, ndigits)

            return result
        return wrapper
    return decorator