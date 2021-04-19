import timeit
from functools import wraps


def pretty_args(d: dict):
    return "   ".join(map(lambda x: f"{x[0]}: {x[1]}" if x[1] and not isinstance(x[1], list) else "", d.items()))


def timer(func):
    @wraps(func)
    def new_function(self, *args, **kwargs):
        start_time = timeit.default_timer()
        res = func(self, *args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        return res, elapsed * 1000

    return new_function
