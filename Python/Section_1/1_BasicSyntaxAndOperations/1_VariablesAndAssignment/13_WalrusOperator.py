
## Python: 1.1.1.13 - Walrus Operator


# Since Python 3.8, we can use the walrus operator to assign variables inside an expression
if (n := len([1, 2, 3])) > 4:
    print(f"List has {n} elements.")
else:
    print("List has less than 4 elements.")
