"""
Topic: Dictionaries in Python

- Stores data in key-value pairs
- Mutable (can be changed)
- Keys are unique
- Values can be of any data type
- Very fast lookup
-Dictionaries are described using curly braces {}
"""

# 1️⃣ Creating a dictionary
student = {
    "name": "Luffy",
    "age": 19,
    "crew": "Straw Hats"
}

print(student)

# 2️⃣ Accessing values
print(student["name"])        # direct access (key must exist)
print(student.get("age"))     # safe access
print(student.get("bounty"))  # returns None if key not found
print(student.get("bounty", "Not Assigned"))

# 3️⃣ Adding new key-value pairs
student["bounty"] = "3 Billion Berries"
student["rank"] = "Yonko"
print(student)

# 4️⃣ Updating values
student["age"] = 20
print(student)

# 5️⃣ Removing items
removed_age = student.pop("age")   # removes and returns value
print("Removed age:", removed_age)
print(student)

# Safe removal (no error if key not present)
student.pop("power", None)

# 6️⃣ Looping through dictionary

# Loop keys
for key in student.keys():
    print("Key:", key)    # key is just variable name it can have name like mango or anything

# Loop values
for value in student.values():
    print("Value:", value)

# Loop key-value pairs (MOST IMPORTANT)
for key, value in student.items():
    print(key, ":", value)

# 7️⃣ Checking if key exists
print("name" in student)
print("power" in student)

# 8️⃣ Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# 9️⃣ Nested dictionary (real-world use)
player = {
    "name": "Zoro",
    "stats": {
        "strength": 95,
        "speed": 85,
        "endurance": 90
    }
}

print(player["stats"]["strength"])

# 🔟 Converting list of tuples to dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]
converted_dict = dict(pairs)
print(converted_dict)

# 🧪 Practice (try yourself)
# 1. Create a dictionary for a book (title, author, price)
# 2. Add a new key
# 3. Update a value
# 4. Loop and print all key-value pairs
