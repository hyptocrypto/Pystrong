from .exceptions import DataFormatCheckError


def check_data_types(**kwargs):
    type_format = kwargs.get("type_format")
    data = kwargs.get("data")
    if not data or not type_format:
        raise DataFormatCheckError(
            "Arguments type_format and data are required. Example: check_data_types(data=[1,2,3], type_format=[int, int, int])"
        )
    if type(data) is not list:
        raise DataFormatCheckError("Please pass data and type_format as a list")

    if len(data) != len(type_format):
        raise DataFormatCheckError("Length of arguments data and type format differ.")

    checks = [type(datapoint) is _type for datapoint, _type in zip(data, type_format)]
    return all(checks)
