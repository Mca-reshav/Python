#set: unordered collection so we cannot access it as usual array 
my_set = {"hello", "world"}
#set = set(["c", "d", "c"])
#print(my_set[0])

#frozenset: immutable objects
frozen_set = frozenset(["a","b"])
#frozen_set.add("c")

#adding element
people = {"Jay", "Idrish", "Archi"}
print(people)
people.add("Daxit")
for i in range(1, 6):
    people.add(i)
print(people)

#union
set1 = {"a", "b"}
set2 = {"c", "d"}
print(set1|set2)
print(set1.union(set2))

#intersection
set1 = set()
set2 = set()
 
for i in range(5):
    set1.add(i)
for i in range(3,9):
    set2.add(i)
set3 = set1.intersection(set2)
print(set3)
set3 = set1 & set2
print(set3)

#difference
print(set2-set1)
print(set2.difference(set1))

#clear
print(set1)
set1.clear()
print(set1)