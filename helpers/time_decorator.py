from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        start = time()
        result = f(*args, **kw)
        end = time()
        print(f"--- {f.__name__} took {end - start:.2f}s seconds ---")

        return result

    return wrap
