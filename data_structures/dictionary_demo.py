"""
dictionary_demo.py
-----------------
Demonstrates Python dictionary operations.

Python Dictionary:
- A dictionary is an **unordered collection of key-value pairs**.
- Keys must be **unique and hashable** (strings, numbers, tuples, etc.).
- Values can be of **any type**: numbers, strings, lists, other dictionaries, objects.
- Dictionaries are **mutable**, so you can add, update, or remove key-value pairs.
- Common use cases: storing structured data, fast lookup by key, configuration storage.

This demo covers:
- Creating dictionaries (including empty and nested dictionaries)
- Accessing and updating elements
- Adding and removing key-value pairs
- Iterating over keys, values, and items
- Dictionary comprehensions
- Using dictionaries as a data structure for structured information
- Using mixed-type keys
"""

# ---------------------------
# 1. Creating Dictionaries
# ---------------------------
print("1. Creating Dictionaries")

person = {"name": "Alice", "age": 30, "city": "Tokyo"}
print("Person dictionary:", person)

empty_dict = {}
print("Empty dictionary:", empty_dict)

people = {
    "Alice": {"age": 30, "city": "Tokyo"},
    "Bob": {"age": 25, "city": "Osaka"}
}
print("Nested dictionary:", people)

# ---------------------------
# 2. Accessing Elements
# ---------------------------
print("\n2. Accessing Elements")

print("Person's name:", person["name"])
print("Person's age using get():", person.get("age"))
print("Non-existent key using get():", person.get("country", "Unknown"))

# ---------------------------
# 3. Adding & Updating Elements
# ---------------------------
print("\n3. Adding & Updating Elements")

person["country"] = "Japan"   # add new key
person["age"] = 31            # update existing key
print("Updated person dictionary:", person)

# ---------------------------
# 4. Removing Elements
# ---------------------------
print("\n4. Removing Elements")

del person["city"]             # remove by key
print("After del city:", person)

removed_value = person.pop("country")  # remove and return value
print("Removed country:", removed_value)
print("Person after pop:", person)

# ---------------------------
# 5. Iterating
# ---------------------------
print("\n5. Iterating")

print("Keys:")
for key in person.keys():
    print(key)

print("Values:")
for value in person.values():
    print(value)

print("Items:")
for key, value in person.items():
    print(f"{key}: {value}")

# ---------------------------
# 6. Dictionary Comprehension
# ---------------------------
print("\n6. Dictionary Comprehension")

squares = {x: x*x for x in range(5)}
print("Squares dictionary:", squares)

# ---------------------------
# 7. Nested Dictionaries Access
# ---------------------------
print("\n7. Nested Dictionaries Access")

for name, info in people.items():
    print(f"{name}: Age={info['age']}, City={info['city']}")

# ---------------------------
# 8. Mixed-Type Keys
# ---------------------------
print("\n8. Mixed-Type Keys")

mixed_keys = {
    "name": "Alice",       # str key
    42: "Answer",          # int key
    (1, 2): "Tuple key",   # tuple key
    True: "Boolean key"    # bool key
}

print("Dictionary with mixed-type keys:", mixed_keys)
print("Access string key:", mixed_keys["name"])
print("Access int key:", mixed_keys[42])
print("Access tuple key:", mixed_keys[(1, 2)])
print("Access boolean key:", mixed_keys[True])
