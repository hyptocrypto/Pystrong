import pytest
from src.pystrong import check_return_types
from src.pystrong.exceptions import EnforcedReturnTypeError

# Should pass
@check_return_types(str)
def return_str():
    return "hello"


@check_return_types(int)
def return_int():
    return 33


@check_return_types(type)
def return_type():
    return bool


@check_return_types(int, str, dict, list)
def return_multiple():
    return 33, "hello", {}, []


# Should fail
@check_return_types(int)
def return_wrong_type():
    return "hello"


@check_return_types(int, str, dict, list)
def return_wrong_multiple():
    return "hello", "hello", 33, 3.34


@check_return_types(int, str, dict)
def return_wrong_lengths():
    return 33


with pytest.raises(EnforcedReturnTypeError):

    # Fail on check that all args are valid python types
    @check_return_types("error")
    def return_error():
        return "error"

    return_error()


def test_check_return_types():
    assert return_str()
    assert return_int()
    assert return_type()
    assert return_multiple()

    with pytest.raises(EnforcedReturnTypeError):
        return_wrong_type()

    with pytest.raises(EnforcedReturnTypeError):
        return_wrong_lengths()

    with pytest.raises(EnforcedReturnTypeError):
        return_wrong_multiple()
