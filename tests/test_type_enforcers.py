from src.pystrong.constants import TYPE_ATTR_FORMAT
from src.pystrong.exceptions import EnforcedTypeError, BadTypeError
from src.pystrong import TypeEnforcer, InferredTypeEnforcer
import pytest

clean_data = {"name": "Jake", "age": 20, "height": 6.2, "books": ["Moby Dick", "For whom the bell tolls", "Crime and punishment"]}
dirty_data = {"name": 33, "age": "hello", "height": ["One", "Two"], "books": "Books"}


class TypedPerson(TypeEnforcer):
    def __init__(self, name, age, height, books):
        super().__init__(name=str, age=int, height=float, books=list)
        self.name = name
        self.age = age
        self.height = height
        self.books = books
        
class InferredPerson(InferredTypeEnforcer):
    def __init__(self, name, age, height, books):
        self.name = name
        self.age = age
        self.height = height
        self.books = books

def test_init_typed_person():
    with pytest.raises(BadTypeError):
        class BadInitTypedPerson(TypedPerson):
            def __init__(self, name, age, height, books):
                super().__init__(name="Test", age=int, height=float, books=list)
                self.name = name
                self.age = age
                self.height = height
                self.books = books
        p = BadInitTypedPerson(**clean_data)
    
def test_clean_typed_enforcer():
    # The clean data should create a valid Person instance
    p = TypedPerson(**clean_data)
    assert(isinstance(p, TypedPerson))
    
    # Trying to set one of the attrs to an improper type should throw an error
    with pytest.raises(EnforcedTypeError):
        p.name = 500
    
def test_dirty_typed_person():
    # The dirty data should throw an EnforcedTypeError when tyrhing to instantiate a instance with improper types.
    with pytest.raises(EnforcedTypeError):
        TypedPerson(**dirty_data)
        
        
def test_inferred_person():
    # should create a valid Person instance
    p = InferredPerson(**clean_data)
    assert(isinstance(p, InferredPerson))
    
    # Trying to set one of the attrs to an improper type should throw an error
    with pytest.raises(EnforcedTypeError):
        p.name = 500
    
    # Can set a new value, and type will be set
    p.new_attr = {"key": "value"}
    with pytest.raises(EnforcedTypeError):
        p.new_attr = 500
        
    # Can delete attr and private type attribute will be deleted as well
    del p.new_attr
    assert not (hasattr(p, "new_attr"))
    assert not (hasattr(p, TYPE_ATTR_FORMAT.format("new_attr")))
    
    