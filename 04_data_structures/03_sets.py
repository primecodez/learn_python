"""
Topic: Sets in Python
Description:
- Unordered collection
- Mutable
- Stores UNIQUE elements only
- Described with curly braces {} or the set() function
"""

# 1️⃣ Creating sets
numbers = {1, 2, 3, 4, 6, 8}
duplicates = {1, 2, 2, 3, 3, 5, 7}

print(numbers)
print(duplicates)   # duplicates are removed automatically

# Creating an empty set (IMPORTANT)
empty_set = set()   # {} creates a dictionary, not a set
print(empty_set)
print(type(empty_set))

# 2️⃣ Adding elements
numbers.add(5)
print(numbers)

# 3️⃣ Removing elements
numbers.remove(3)    # error if element not found
numbers.discard(10)  # no error if element not found
print(numbers)

# 4️⃣ Checking membership
print(2 in numbers)
print(100 in numbers)

# 5️⃣ Looping through a set
for num in numbers:
    print(num)

# 6️⃣ Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)          # {1, 2, 3, 4, 5}
print("Intersection:", a & b)   # {3}
print("Difference:", a - b)     # {1, 2}
print("Symmetric Difference:", a ^ b)  # {1, 2, 4, 5}

# 7️⃣ Converting list to set (remove duplicates)
list_with_dupes = [1, 2, 2, 3, 4, 4]
unique_items = set(list_with_dupes)
print(unique_items)
