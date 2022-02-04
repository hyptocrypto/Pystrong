import pytest
from src.pystrong import check_data_types
from src.pystrong.exceptions import DataFormatCheckError


clean_data = [
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
]
dirty_data = [
    [1, "hello", {}],
    ["hello", "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
]
unequal_len_data = [
    [1, "hello", {}, 33, 45],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
    [1, "hello", {}],
]

clean_type_format = [int, str, dict]
dirty_type_format = [int, str, str]
unequal_len_type_format = [int, str, dict, list]


def test_data_checker():
    success = all(
        [check_data_types(data=d, type_format=clean_type_format) for d in clean_data]
    )
    fail_dirty_data = all(
        [check_data_types(data=d, type_format=clean_type_format) for d in dirty_data]
    )
    fail_dirty_format = all(
        [check_data_types(data=d, type_format=dirty_type_format) for d in clean_data]
    )
    assert success
    assert not fail_dirty_data
    assert not fail_dirty_format
    with pytest.raises(DataFormatCheckError):
        fail_unequal_len_type_format = all(
            [
                check_data_types(data=d, type_format=unequal_len_type_format)
                for d in clean_data
            ]
        )
