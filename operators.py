#division
print(8/3)  #float
print(8//3) #floor

#Membership Operators
x = 24
y = 20
list = [10, 20, 30, 40, 50] 
  
if (x not in list): #not in just like array.includes
    print("x is NOT present in given list") 
else: 
    print("x is present in given list") 
  
if (y in list): 
    print("y is present in given list") 
else: 
    print("y is NOT present in given list") 


#ternary operators: ?: in js
a,b = 10, 20
min = a if a<b else b
print(min)

a, b = 11, 21
print( (b, a) [a < b] )

a, b = 32, 22
print({True: a, False: b} [a < b])

#Operator Overloading
print(1+2)
print("hello"+"world")
print(3*4)
print("hello\n"*4)

#Binary operator overloading

class complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
Obj1 = complex(1,2)
Obj2 = complex(2,3)
Obj3 = Obj1 + Obj2
print(Obj3)

#any(): returns true if any of the items is True 
#and return False if empty or all are false
print (any([False, False, False]))
print (any([False, True, False]))

list1, list2 = [], []
for i in range(1,11):
    list1.append(4*i)

for i in range(0,len(list1)):
    list2.append(list1[i]%5==0)
print("check divisible by 5", any(list2))

#all return True if all of the items are True or empty
print (all([True, True, True]))

#operator functions: basic functions
import operator
print(operator.add(1,2))
print(operator.sub(1,2))
print(operator.mul(1,2))

print(operator.truediv(1,2))
print(operator.floordiv(1,2))
print(operator.pow(1,2))
print(operator.mod(1,2))

print(operator.lt(1,2))
print(operator.le(1,2))
print(operator.eq(1,2))
print(operator.ne(1,2))

#setitem(), delitem() and getitem()
list = [1, 2, 3, 4]
print("Original list:",list)
operator.setitem(list, 3, 30)
print("after setitem():",list) 
operator.setitem(list,slice(1,4),[21,33,40])
print("after setitem():",list) 
operator.delitem(list,slice(2,4)) 
print("after delitem():",list)
print(operator.getitem(list, 1))
str1 ="say hello world"
str2 ="world"
print(operator.concat(str1, str2))
print(operator.contains(str1, str2))

# == Operator and "is" operator
a=[]
b=[]
c=a
print(a==b) #== to compare by value
print(a is b) #is to compare by identity
print(id(a), id(b))
