from .exceptions import EnforcedReturnTypeError


def check_return_type(ret_type):
    if type(ret_type) is not type:
        raise EnforcedReturnTypeError("Check return type argument must be a valid python type.")
    def wrapper(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            if type(ret) != ret_type:
                raise EnforcedReturnTypeError(
                    f"Function '{func.__name__}' returned type {type(ret)}. Expected return type is {ret_type}."
                )
            return func(*args, **kwargs)

        return inner

    return wrapper
