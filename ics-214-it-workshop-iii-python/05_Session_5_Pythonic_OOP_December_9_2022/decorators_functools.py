# The definition for decorators goes here.
from time import time
from functools import wraps


def time_it_preserve(decorated_function):
    @wraps(decorated_function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = decorated_function(*args, **kwargs)
        end_time = time()
        print(
            f"Function {decorated_function.__name__} took {end_time - start_time}s to execute."
        )  # Note: We make use of Python Introspection here for getting the name of the function in the f-String.
        return result

    return wrapper
