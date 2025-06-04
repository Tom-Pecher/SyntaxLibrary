
## Python: 1.1.1.11 - Global and Local Variables


# Global variables can be accessed anywhere in the code (global scope).
x = "global"

# Local variables can only be accessed in their section of code (local scope)
def func():
    x = "local"
    print(x)

func()     # Prints "local"
print(x)   # Prints "global"

# To make a local variable global, use the global keyword:
def change():
    global x
    x = "changed globally"
