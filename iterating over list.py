#remove() method removes the first occurrence of the specified value from the list. If the value is not found, it raises a ValueError.
a=[1,2,3,4,5,2,2,4,5,3,5,6,7,8,9,10]
a.remove(2)
print(a)
#pop() method removes the item at the given index from the list and returns the removed item. If no index is specified, pop() removes and returns the last item in the list.
a.pop(3)
print(a)
a.pop()
print(a)
#clear() method removes all items from the list.
a.clear()   
print(a)