from typing import List, Dict,Tuple,Type, Any
from exceptions import EnforceredTypeError, AttributeTypeNotSet, BadTypeError, InitError
from constants import ATTR_TYPE

class InferredTypeEnforcer:
    """
    This class is to be used as a base class to derive a type enforced child class.
    Types will be inferred from the values passed. The call to super().__init__ requires
    the attrs to be passed in the (a=a, b=b) manner.
    Example:
        class Person(ExplicitTypeEnforcer):
            def __init__(self, name, age):
                super().__init__(name=name, age=age)
                self.name = name
                self.age = age
    """    
    
    def __init__(self, *args, **kwargs):
        if args and not kwargs:
            raise InitError(f"Args {args} must be passed to super().__init__ as kwargs i.e. key value pairs.")
        for attr_name, value in kwargs.items():
            self.__dict__.update({ATTR_TYPE.format(attr_name): type(value)})

    def __setattr__(self, key: str, value: Any) -> None:
        if not self.__dict__.get(ATTR_TYPE.format(key)):
            raise AttributeTypeNotSet(f"No type for attr '{key}' set. This is most likely due to not calling super in the derived class constructor.")
        
        if type(value) is not getattr(self, ATTR_TYPE.format(key)):
            raise EnforceredTypeError(f"Cant not set type: {type(value)} for attribute '{key}'")
        super().__setattr__(key, value)
        

class ExplicitTypeEnforcer:
    """
    This class is to be used as a base class to derive a type enforced child. 
    Pass kwargs as (attr_name, type) key value pairs to the super constructor.
    Example:
        class Person(ExplicitTypeEnforcer):
            def __init__(self, name, age):
                super().__init__(name=str, age=int)
                self.name = name
                self.age = age
    """
    
    def __init__(self, **kwargs):
        for attr_name, _type in kwargs.items():
            if not isinstance(type(_type), type):
                raise BadTypeError("Key word arguments must be in (attr_name, type) format. Ensure 'type' is a valid python type.")
            self.__dict__.update({ATTR_TYPE.format(attr_name): _type})
            
    def __setattr__(self, key: str, value: Any) -> None:
        if not self.__dict__.get(ATTR_TYPE.format(key)):
            raise AttributeTypeNotSet(f"No type for attr '{key}' set. This is most likely due to not calling super in the derived class constructor.")
        
        if type(value) is not getattr(self, f"___{key}_type"):
            raise EnforceredTypeError(f"Cant not assign type: {type(value)} to attribute '{key}'. Must be of type: {getattr(self, f'___{key}_type')}")
        super().__setattr__(key, value)
