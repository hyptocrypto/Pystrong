from .exceptions import EnforcedReturnTypeError, EnforcedArgTypeError


def check_return_type(*ret_types):
    for _type in ret_types:
        if type(_type) is not type:
            raise EnforcedReturnTypeError(
                f"Check return type arguments must be a valid python type. Please check '{_type}'"
            )

    def wrapper(func):
        def inner(*args, **kwargs):
            retruns = func(*args, **kwargs)
            for ret, ret_type in zip(retruns, ret_types):
                if type(ret) != ret_type:
                    raise EnforcedReturnTypeError(
                        f"Function '{func.__name__}' returned '{ret}' of type '{type(ret)}'. Expected return type is '{ret_type}'."
                    )
            return func(*args, **kwargs)

        return inner

    return wrapper


def check_arg_type(*type_args):
    for _type in type_args:
        if type(_type) is not type:
            raise EnforcedArgTypeError(
                "Check argument type argument must be a valid python type."
            )

    def wrapper(func):
        def inner(*args):
            for _type, arg in zip(type_args, args):
                if type(arg) is not _type:
                    raise EnforcedArgTypeError(
                        f"Argument '{arg}' must be of type {_type}"
                    )
            return func(*args)

        return inner

    return wrapper
