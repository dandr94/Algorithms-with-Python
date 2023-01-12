from typing import Any, Callable
from time import perf_counter

"""
Context manager that tracks time execution of recursive function.
"""


class Timeit:

    def __init__(self, func: Callable) -> None:
        self.func = func
        self.timed = []

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        start = perf_counter()
        res = self.func(*args, **kwargs)
        end = perf_counter()
        self.timed.append(end - start)
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # TODO: report `exc_*` if an exception get raised
        print(f"--- {self.func.__name__} took {sum(self.timed):.2f}s seconds ---")
        return
