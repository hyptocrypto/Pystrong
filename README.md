# Pystrong. Type enforcement for python objects

## Example
Use the ExplicitTypeEnforcer class as a base class for your derived, and the types you set for the attributes will be enforced throughout the life of the object.

```
from pystrong import ExplicitTypeEnforcer

class Person(ExplicitTypeEnforcer):
    def __init__(self, name, age):
        super().__init__(name=str, age=int)
        self.name = name
        self.age = age

p = Person('Jake', 32)
p.name = 55

EnforceredTypeError: Cant not set type: <class 'int'> for attribute 'name'
```

