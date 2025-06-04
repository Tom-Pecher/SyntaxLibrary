
## Python: 1.1.1.9 - Mutability


# Variables are immutable by default:
x = 5
x = 6
# In the previous code, the value of x is not changed.
# Instead, a new variable x is created with the value 6.

# Hence, after the following is run, b is still 10 despite a being reassigned to 20:
a = 10
b = a
a = 20

# Lists, however, are mutable:
lst1 = [1, 2, 3]
lst2 = lst1
lst1.append(4)
# In the previous code, both lst1 and lst2 are now [1, 2, 3, 4].


# Mutable types:
    # lists
    # sets
    # dictionaries
    # user-defined classes

# Immutable types:
    # integers
    # floats
    # strings
    # tuples
    # frozensets
    # bytes
    # complex
    # bool
