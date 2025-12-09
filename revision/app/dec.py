import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        elapsed = (end - start).total_seconds()

        print(f"{func.__name__} took {elapsed:.3f} seconds")
        return result
    return wrapper
