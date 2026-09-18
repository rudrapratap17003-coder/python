#list is mutable and we can change the value of list after it is created. we can add, remove, or change items in a list after it is created.
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)
#updating the list by adding new item
fruits[2] = "banana"
print(fruits)
#updated a slice range
fruits[0:2] = ["kiwi", "mango"]
print(fruits)
