import pytest
from src.pystrong import check_return_type
from src.pystrong.exceptions import EnforcedReturnTypeError



@check_return_type(str)
def return_str():
    return "hello"

@check_return_type(int)
def return_int():
    return 33

@check_return_type(int)
def return_wrong_type():
    return "hello"

with pytest.raises(EnforcedReturnTypeError):
    @check_return_type("error")
    def return_error():
        return 'error'
    return_error()


def test_check_return_type():
    assert(return_str())
    assert(return_int())
        
    with pytest.raises(EnforcedReturnTypeError):
        return_wrong_type()
