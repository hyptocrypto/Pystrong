from typing import List, Dict,Tuple,Type, Any
from exceptions import EnforceredTypeError, AttributeTypeNotSet


class TypeEnforcer:
    """
    This class is used as a base class
    to ensure that derived classes are strongly typed.
    """    
    def __init__(self, *args, **kwargs):
        type_dict = {(f"__{key}_type", type(value)) for key, value in self.__dict__.items()}
        self.__dict__.update(type_dict)

    def __setattr__(self, key: str, value: Any) -> None:
        if not self.__dict__.get(f"__{key}__type"):
            return super().__setattr__(key, value)
        
        if type(value) is not getattr(self, f"__{key}_type"):
            raise EnforceredTypeError(f"Cant not set type: {type(value)} for attribute '{key}'")
        super().__setattr__(key, value)
        
        