"""
list_demo.py
------------
Demonstrates Python list operations:
- Creating lists (including empty lists)
- Adding, removing, and updating items
- Iterating and slicing
- Using lists to store tabular (CSV-like) data
- Storing class objects inside a list
"""

# ---------------------------
# 1. Creating Lists
# ---------------------------
print("1. Creating Lists")

fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)

# Empty list examples
empty1 = []
empty2 = list()
print("Empty list 1:", empty1)
print("Empty list 2:", empty2)

# ---------------------------
# 2. Adding Elements
# ---------------------------
print("\n2. Adding Elements")

fruits.append("date")
print("After append:", fruits)

fruits.extend(["elderberry", "fig"])
print("After extend:", fruits)

fruits.insert(1, "blueberry")
print("After insert:", fruits)

# ---------------------------
# 3. Removing Elements
# ---------------------------
print("\n3. Removing Elements")

fruits.remove("banana")
print("After remove:", fruits)

popped = fruits.pop()
print("After pop:", fruits, "| Popped:", popped)

del fruits[0]
print("After del[0]:", fruits)

# ---------------------------
# 4. Updating & Accessing
# ---------------------------
print("\n4. Updating & Accessing")

fruits[0] = "apricot"
print("Updated list:", fruits)
print("Slice [0:2]:", fruits[0:2])
print("Length:", len(fruits))

# ---------------------------
# 5. Iterating
# ---------------------------
print("\n5. Iterating")

for fruit in fruits:
    print("Fruit:", fruit)

# ---------------------------
# 6. Using an Empty List Dynamically
# ---------------------------
print("\n6. Using an Empty List Dynamically")

dynamic_list = []
for i in range(3):
    dynamic_list.append(i * 10)
print("Dynamic list after loop:", dynamic_list)

# ---------------------------
# 7. Table-like Data (CSV-style)
# ---------------------------
print("\n7. Table-like Data (CSV-style)")

# Each inner list represents a row in a CSV
table = [
    ["Name",  "Age", "City"],
    ["Alice", 30,   "Tokyo"],
    ["Bob",   25,   "Osaka"],
    ["Cara",  28,   "Nagoya"]
]

for row in table:
    print(row)

# Access individual cells
print("Cell [1][0] (Name of 2nd row):", table[1][0])

# ---------------------------
# 8. List of Class Objects
# ---------------------------
print("\n8. List of Class Objects")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # In Python, __repr__ is a special (dunder) method that defines the official string representation of an object.
    # Used for debugging and logging.
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

for person in people:
    print(person) # Call

# ---------------------------
# 9. Mixed-Type Lists
# ---------------------------
print("\n9. Mixed-Type Lists")

mixed_list = [42, "apple", 3.14, True, None, [1, 2, 3], {"key": "value"}]
print("Mixed list:", mixed_list)

# Accessing different types
print("Integer element:", mixed_list[0])
print("String element:", mixed_list[1])
print("Float element:", mixed_list[2])
print("Nested list element:", mixed_list[5])
print("Dictionary element:", mixed_list[6])