#Take user input and return output
name = input("Enter your name: \n")
print("hello"+" " +name)

#cast the input 
floatNum = float(input("Enter a decimal number: ")) 
print(floatNum, " ", type(floatNum)) 

#split(): to take multiple inputs
x,y = input("enter the values: \n").split()
print("nums are {} and {}".format(x,y))

#output
name = "Alice"
age = 25
print("Hello, my name is", name, "and I am", age, "years old.")

#end= parameter in print()
print("hello",end="world")

#write file in print
print("hello world", file=open('writeFile.py','w'))

#sep=
print('01','01','2024', sep='-', end='\n')