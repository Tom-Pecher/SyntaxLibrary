
## Python: 1.1.3.5 - Concatenation Techniques


# We can use the + operator to concatenate strings (and only strings):
print("Hello " + "world!") # Hello world!


# We can also use the string format method to concatenate strings:
name, age = "Alice", 30
print("Name: {} | Age: {}".format(name, age)) # Name: Alice | Age: 30

# We can also set the order of insertion using index or keyword placeholders:
print("Age: {1} | Name: {0}".format(name, age)) # Age: 30 | Name: Alice
print("Name: {n} | Age: {a}".format(n=name, a=age)) # Name: Alice | Age: 30


# However, it is almost always simply better to use f-strings (introduced in Python 3.6):
print(f"Name: {name} | Age: {age}") # Name: Alice | Age: 30
