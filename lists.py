#lists: dynamically sized arrays
List = [['Hello', 'world'], ['Hello']]
print(List[0][1])
print(List[1][0])

#append: add elements at the end of lists
list = []
list.append(1)
list.append(("apple", "banana"))
list.append(["hello", 10])
print(list)

#insert: to add element at any desired position
list.insert(2,100)
print(list)

#extend: to add multiple element at the same time
list.extend([3, 'say'])
print(list)

#reverse a list using: reverse() and reversed()
List = ['a', 'b', 'c']
List.reverse()
print(List)

#remove: to remove an element from a list
List.remove('a')
print(List)

#pop: to remove from specific position
List.pop(1)
print(List)