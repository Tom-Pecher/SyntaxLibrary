
## Python: 1.1.2.14 - Memory View


# The memoryview type is a read-only view of a buffer:
b = bytearray(b'hello')
mv = memoryview(b)
mv[0] = 71  # Changes b to b'Gello'
