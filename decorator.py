from datetime import datetime
from functools import wraps


def logger(enabled):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                print("calling function: " + func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def afterbefore(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("before {} called".format(func.__name__))
        func(*args, **kwargs)
        print("after {} called".format(func.__name__))

    return wrapper


def timeit(func):
    # @wraps(func)
    def timed(*args, **kwargs):
        ts = datetime.now()
        result = func(*args, **kwargs)
        te = datetime.now()

        print("took {!s}".format(te - ts))
        return result

    return timed


@afterbefore
@timeit
@logger(True)
def greeting(name):
    print("Hello {}".format(name))


greeting("ali")
print("greeting function name = {}".format(greeting.__name__))
