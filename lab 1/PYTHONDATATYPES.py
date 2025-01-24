x = "Hello World"
print(x, type(x)) #string
x1 = 20
print(x1, type(x1)) #integer
x2 = 20.5
print(x2, type(x2)) #float
x3 = 1j
print(x3, type(x3)) #complex
x4 = ["apple", "banana", "cherry"]
print(x4, type(x4)) #list
x5 = ("apple", "banana", "cherry")
print(x5, type(x5)) #tuple
x6 = range(6)
print(x6, type(x6)) #range
x7 = {"name" : "John", "age" : 36}
print(x7, type(x7)) #dict
x8 = {"apple", "banana", "cherry"}
print(x8, type(x8)) #set
x9 = frozenset({"apple", "banana", "cherry"})
print(x9, type(x9)) #frozenset 
x10 = True
print(x10, type(x10)) #bool
x11 = b"Hello"
print(x11, type(x11)) #bytes
x12 = bytearray(5)
print(x12, type(x12)) #bytearray
x13 = memoryview(bytes(5))
print(x13, type(x13)) #memoryview
x14 = None
print(x14, type(x14)) #NoneType