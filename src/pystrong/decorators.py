from .exceptions import EnforcedReturnTypeError, EnforcedArgTypeError


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


def check_arg_type(*type_args):
    for _type in type_args:
        if type(_type) is not type:
            raise EnforcedArgTypeError("Check argument type argument must be a valid python type.")
    def wrapper(func):
        def inner(*args):
            for _type, arg in zip(type_args, args):
                if type(arg) is not _type:
                    raise EnforcedArgTypeError(f"Argument {arg} must be of type {_type}")
            return func(*args)
        return inner
    return wrapper
