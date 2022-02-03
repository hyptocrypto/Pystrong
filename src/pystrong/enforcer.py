from typing import Any

from .constants import TYPE_ATTR_FORMAT
from .exceptions import AttributeTypeNotSet, BadTypeError, EnforcedTypeError, InitError


class TypeEnforcer:
    """
    This class is to be used as a base class to derive a type enforced child.
    Pass kwargs as (attr_name, type) key value pairs to the super constructor.
    Example:
        class Person(TypeEnforcer):
            def __init__(self, name, age):
                super().__init__(name=str, age=int)
                self.name = name
                self.age = age
    """

    def __init__(self, *args, **kwargs):
        if args and not kwargs:
            raise InitError("Arguments must be based as kwargs, i.e key value pairs.")
        for attr_name, _type in kwargs.items():
            if type(_type) is not type:
                raise BadTypeError(
                    "Key word arguments must be in (attr_name, type) format. Ensure 'type' is a valid python type."
                )
            self.__dict__.update({TYPE_ATTR_FORMAT.format(attr_name): _type})

    def __setattr__(self, key: str, value: Any) -> None:
        if not self.__dict__.get(TYPE_ATTR_FORMAT.format(key)):
            raise AttributeTypeNotSet(
                f"No type for attr '{key}' set. This is most likely due to not calling super in the derived class constructor."
            )

        if type(value) is not getattr(self, f"___{key}_type"):
            raise EnforcedTypeError(
                f"Cant not assign type: {type(value)} to attribute '{key}'. Must be of type: {getattr(self, f'___{key}_type')}"
            )
        super().__setattr__(key, value)

    def __delattr__(self, key: str):
        del self.__dict__[TYPE_ATTR_FORMAT.format(key)]
        super().__delattr__(key)


class InferredTypeEnforcer(object):
    """
    This class is to be used as a base class to derive a type enforced child class.
    Types will be inferred from the values passed.
    """

    def __setattr__(self, key: str, value: Any) -> None:
        if not self.__dict__.get(TYPE_ATTR_FORMAT.format(key)):
            self.__dict__.update({TYPE_ATTR_FORMAT.format(key): type(value)})
            super().__setattr__(key, value)

        if type(value) is not getattr(self, TYPE_ATTR_FORMAT.format(key)):
            raise EnforcedTypeError(
                f"Cant not set type: {type(value)} for attribute '{key}'"
            )
        super().__setattr__(key, value)

    def __delattr__(self, key: str):
        del self.__dict__[TYPE_ATTR_FORMAT.format(key)]
        super().__delattr__(key)
