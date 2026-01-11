"""
Dictionaries in Python

A dictionary stores data in key-value pairs.

Key features:
- Keys are UNIQUE
- Values can be any data type
- Unordered (in older Python versions)
- Very fast lookup using keys
-Dictionaries are mutable (can be changed)
-Dictories are defined using curly braces {}

"""

# 1️⃣ Creating a dictionary
student = {
    "name": "Alex",
    "age": 20,
    "course": "Python"
}

print("Student dictionary:", student)


# 2️⃣ Accessing values using keys
print("Name:", student["name"])
print("Age:", student["age"])


# 3️⃣ Using get() method (safe access)
print("Course:", student.get("course"))
print("City:", student.get("city"))      # Returns None (no error)
print("City:", student.get("city", "NA"))  # Default value


# 4️⃣ Adding new key-value pairs
student["city"] = "Delhi"
print("After adding city:", student)


# 5️⃣ Updating existing values
student["age"] = 21
print("After updating age:", student)


# 6️⃣ Removing elements
student.pop("city")     # Remove by key
print("After removing city:", student)


# 7️⃣ Looping through dictionary

# Loop through keys
for key in student:
    print("Key:", key)

# Loop through values
for value in student.values():
    print("Value:", value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, "->", value)


# 8️⃣ Checking if a key exists
print("name" in student)
print("marks" in student)


# 9️⃣ Dictionary length
print("Number of items:", len(student))


# 🔟 Nested dictionary
students = {
    1: {"name": "Alex", "age": 20},
    2: {"name": "Bob", "age": 22}
}

print("Nested dictionary:", students)
print("Student 1 name:", students[1]["name"])


# ✅ End of dictionary basics
