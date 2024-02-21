# There is no command for declaring a variable
x=5     #typeof integer
y="hello"   #typeof string

#casting of variables

x=str(3)    #x will be '3'
x=float(3)  #x will be 3.0

#type(): to get datatype

print(type(x))

#Both single and double quotes are allowed

#variable names: case-sensitive and must start with letter or underscore
#variable names cases: camel, pascal and snake case

#many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables
x=y=z = "apple"

#unpacking: to extract collection of values, similar like destructuring in js
fruits = ["apple", "grapes", "orange"]
x,y,z = fruits
print(x,y,z)

#output: you cannot use to print sum of integer and string like:
x=5
y="hello"
#print(x+y)

#Global variables:
x = "awesome"

def myFunc():
  x = "fantastic"
  print("Python is " + x)

myFunc()
print("Python is " + x)

#global keyword: to create a global variable inside a function

def myFunc():
  global x
  x="hello"

myFunc()

print("global", x)

# use the global keyword if you want to change a global variable inside a function

x="hello"

def myFunc():
  global x
  x="hey"

myFunc()

print(x)