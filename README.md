# Pystrong. Type enforcement for python objects

## Usage
Use the ExplicitTypeEnforcer class as a base class and the types you set for the attributes in your derived classes will be enforced throughout the life of the object.

```python
from pystrong import TypeEnforcer

class Person(TypeEnforcer):
    def __init__(self, name, age):
        super().__init__(name=str, age=int)
        self.name = name
        self.age = age

p = Person('Jake', 32)
p.name = 55

EnforcedTypeError: Cant not assign type: <class 'int'> to attribute 'name'. Must be of type: <class 'str'>
```
EnforcedTypeError is thrown because the value of the name attribute on a Person object must always be a string.

When creating the class Person, the first thing the constructor must do is call base classes constructor passing the all attributes with their intended value as key value pairs. Thereafter, the object should behave as normal. 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

