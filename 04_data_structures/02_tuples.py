"""Tuples in Python"""
    - An ordered, unchangeable collection of items.
    - Tuples in Python are displayed using parentheses ()
    - They are immutable (cannot be changed)

# Creating tuples
b=(5,44,7,5,9) 
g=(3.14,"hello",True,55)
h=(55,)  # single element tuple,remember the comma is important 

print(b)
print(g)
print(h)

# Accessing elements in a tuple
print(b[0])
print(h[0])

# Finding length of tuple
print("Length:",len(g))

#Slicing in tuple
print(b[::2]) # prints every 2nd element
print(g[::-2]) # prints every second element in reverse order starting from last element

# Unpacking of tuple
point=(3,4
x,y=point
print("x:",x)
print("y:",y)

#Checking membership in tuple
print(5 in b)  # True
print("python" in g)  # False

sample(1,2,44,5,2,1,7,5)
print("Conut of 2:",sample.count(2)) # counts occurrences of 2
print("Index of 44:",sample.index(44)) # finds index of first occurrence of 44


# Funfact: Tuples are immutable, so you cannot modify, add or remove elements after creation.