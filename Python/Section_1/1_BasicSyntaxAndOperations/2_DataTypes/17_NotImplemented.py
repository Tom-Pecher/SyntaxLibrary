
## Python: 1.1.2.17 - Not Implemented


# The NotImplemented type is used to indicate unsupported operations:
class MyClass:

    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
