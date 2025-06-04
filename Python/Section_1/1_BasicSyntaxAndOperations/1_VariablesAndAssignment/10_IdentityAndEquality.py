
## Python: 1.1.1.10 - Identity and Equality


a = [1, 2, 3]
b = [1, 2, 3]
c = None

# Check if two variables are equal (have the same value):
a == b # True
a == c # False

# Check if two variables are identical (refer to the same object):
a is b # False
a is a # True
