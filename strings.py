#"hello" or 'hello' is same

#strings are arrays: strings are arrays of bytes representing unicode characters

#python does not have a character datatype

#Looping in string
for x in "apple":
    print(x)

#string length
a="say, hello world"
print(len(a))

#check string
msg="I love India"
print("love" in msg)    #output will be True

#check if not
txt="We live young, We live free!"
if "live" not in txt:
    print("if")
else:
    print("else")

#slicing
b="hello, world"
print(b[2:5])   #get characters from position between 2 and 5: llo
print(b[:5])    #get characters from starting position
print(b[2:])    #get characters from position from 2 to end
print(b[-5:-2]) #wor

#case
c="Hello"
print(c.upper())
print(c.lower())

#remove whitespace: strip just like trim in js
d="  h  e y !, you  "
print(d.strip())

#replace
e="hello"
print(e.replace("ello", "ola"))

#split
f="hello, mr!"
print(f.split(","))     #return in list

#concatenate using + operator
print(e+f)

#format(): To combine strings and numbers
name="Reshav"
age=25
txt="My name is {} and I am {} years old"
txt2="My name is {0} and I am {1} years old"
print(txt.format(name, age))
print(txt2.format(name, age))

#escape character
print("hello \"Mr.\" hero")


#single quote: \'
#backslash: \\
#newline: \n
#tab: \t
#backspace: \b
#octal value: \ooo
#hex value: \xhh

#string methods
example="hello dev say hello world"
print(example.capitalize())