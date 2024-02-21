#Build-in datatypes:
"""
Text: str
Numeric: int, float, complex
Sequence: list, tuple, range
Mapping: dict,
Set: set, frozenset
Boolean: bool
Binary: bytes, bytearray, memoryview
None: NoneType

"""

#To get the datatype: just like typeof in js
x=5
print(type(5))

#Datatype: array is list, object is dict and null is None
"""
str: "Hello World"
int: 24
float: 24.5, 35e3 : e is power of 10
complex: 1j : "j" is imaginary
list: ["apple", "banana", "grapes"]
tuple: ("apple", "banana", "cherry")
range(6) : output will be range(0,6)
dict: {"name": "John", "age": 36}
set: {"apple", "banana", "grapes"}
frozenset({{"apple", "banana", "grapes"}})
bool: True
bytes: b"Hello"
bytearray: bytearray(5)
memoryview: memoryview(bytes(5))

"""
#Random Number: Python does not have random() function, but it has built-in module
"""
import random
print(random.randrange(1,10))

"""
#Casting

x=int(1.9)      #output will be 1
x=float("2.3")  #output will be 2.3
x=str(2)        #output will be 2