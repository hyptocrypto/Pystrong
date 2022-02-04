from .exceptions import EnforcedArgTypeError, EnforcedReturnTypeError

non_iterables = [int, float, bool]


def check_return_types(*ret_types):
    # Make sure all args passed to decorator are a valid python type
    if not ret_types:
        raise EnforcedReturnTypeError(
            "Please pass at least one type to check_return_types"
        )
    for _type in ret_types:
        if type(_type) is not type:
            raise EnforcedReturnTypeError(
                "Check return type arguments must be a valid python type. Please check"
                f" '{_type}'"
            )

    def wrapper(func):
        def inner(*args, **kwargs):
            # The return values form the function that is being decorated
            rets = func(*args, **kwargs)
            func_return_types = parse_return_types(rets)

            if len(func_return_types) != len(ret_types):
                raise EnforcedReturnTypeError(
                    "Length of type argument passed to check_return_type is not equal"
                    f" to length of values returned by function '{func.__name__}'"
                )

            # Iter over actual returns and expected returns and check for validity
            for ret, ret_type in zip(func_return_types, ret_types):
                if ret != ret_type:
                    raise EnforcedReturnTypeError(
                        f"Function '{func.__name__}' returned '{func_return_types}'."
                        f" Expected return type format is '{ret_types}'."
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


def parse_return_types(ret):
    # If func returns a actual python type
    if type(ret) is type:
        return [type]

    # If func returns a non iterable such as True, 4, or 23.3
    if type(ret) in non_iterables:
        return [type(ret)]

    # Strings are iterable, but single string should not be iterated
    if type(ret) == str:
        return [str]

    # Return a list of types for the func returns
    return [type(r) for r in ret]
