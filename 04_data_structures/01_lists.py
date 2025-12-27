""" Topic: Lists in python
   - An ordered, changeable collection of items.
   -Lists in Python are displayed using square brackets []
   -They are mutable(can be changed)
   -Are ordered 
   -It allows duplicate elements

"""


# Creating lists
numbers = [1, 4, 4, 5, 7]
mixed = [1, 3.14, False, "telephone"]

print(numbers)
print(mixed)

# Accessing elements in a list
print(numbers[0])
print(mixed[2])

# Modifying elements in list
numbers[1] = 6
print(numbers)

# Adding elements
numbers.append(7)   # add at end
print(numbers)
mixed.insert(2, 10)   # insert at index
print(mixed)

# Removing elements
numbers.remove(7)         # Remove by value
last_item = numbers.pop()  # Remove last element
print(numbers)
print("Popped:", last_item)

# Find length of list using len() function
num = [1, 5, 45, 41]
print("Length:", len(num))

# How to do list slicing
n = [1, 5, 4, 5, 78, 15, 16, 98]
print(n[1:4])  # prints from index 1 to 3
print(n[::3])  # prints every 3rd element
print(n[::-2])  # prints every second element in reverse order starting from last element

# Common list methods
p = [1, 5, 66, 45, 78, 41, 15]
p.sort()
print("Sorted:", p)  # sorts elements in ascending order

p.reverse()
print("Reversed:", p)  # prints list in backward
