# Pystrong. Type enforcement for python objects

## Usage

### BaseClass
Use the <b>TypeEnforcer</b> class as a base class and the types you set for the attributes in your derived classes will be enforced throughout the life of the object.
When creating the class Person, the first thing the constructor must do is call base classes constructor passing the all attributes with their intended value as key value pairs. Thereafter, the object should behave as normal.
```python
from pystrong import TypeEnforcer

class Person(TypeEnforcer):
    def __init__(self, name, age):
        super().__init__(name=str, age=int)
        self.name = name
        self.age = age

p = Person('Jake', 32)
p.name = 55

EnforcedTypeError: Can not assign type: <class 'int'> to attribute 'name'. Must be of type: <class 'str'>
```
EnforcedTypeError is thrown because the value of the name attribute on a Person object must always be a string.
 
### Decorators
There are also some handy decorators to ensure that a method arguments are the right type, or that the method returns the proper type. Using the <b>check_return_type</b> decorator will throw an error if the method returns an invalid type.
```python
from pystrong import check_return_type

@check_return_type(str, int)
def test_success():
    return "Hello World", 500

@check_return_type(str, int)
def test_fail():
    return 500, {"test": "error"}

test_success()
("Hello World", 500)

test_fail()
EnforcedReturnTypeError: Function 'test_fail' returned '500' of type '<class 'int'>'. Expected return type is '<class 'str'>'.
```
The <b>check_arg_type</b> decorator can be used to enforce that arguments to the function are of the proper type.
```python
from pystrong import check_arg_type

@check_arg_type(int, str)
def add_10(num, string):
    print(string)
    return num+10

@check_arg_type(int, str)
def error(num, string):
    print(string)
    return "error"

add_10(5, "Hello World")
Hello World
15

add_10("throw", "error")
EnforcedArgTypeError: Argument 'throw' must be of type <class 'int'>
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please update tests accordingly. 

## License
[MIT](https://choosealicense.com/licenses/mit/)

