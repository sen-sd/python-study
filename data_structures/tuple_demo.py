"""
tuple_demo.py
-------------
Demonstrates Python tuple operations:
- Creating tuples (including empty and single-element tuples)
- Accessing elements and slicing
- Immutability
- Packing and unpacking
- Nesting tuples
- Using tuples as dictionary keys
"""

# ---------------------------
# 1. Creating Tuples
# ---------------------------
print("1. Creating Tuples")

numbers = (1, 2, 3)
mixed = (42, "apple", 3.14)
empty_tuple = ()
single_element = (5,)  # NOTE: comma is required for a single-element tuple

print("Numbers tuple:", numbers)
print("Mixed tuple:", mixed)
print("Empty tuple:", empty_tuple)
print("Single-element tuple:", single_element)

# ---------------------------
# 2. Accessing Elements
# ---------------------------
print("\n2. Accessing Elements")

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice [0:2]:", numbers[0:2])

# ---------------------------
# 3. Immutability
# ---------------------------
print("\n3. Immutability")

# Tuples cannot be modified directly
try:
    numbers[0] = 10
except TypeError as e:
    print("Error when trying to modify:", e)

# But you can create a new tuple
new_numbers = numbers + (4, 5)
print("Concatenated tuple:", new_numbers)

# ---------------------------
# 4. Packing and Unpacking
# ---------------------------
print("\n4. Packing and Unpacking")

person = ("Alice", 30, "Tokyo")  # packing
name, age, city = person         # unpacking
print(f"Name: {name}, Age: {age}, City: {city}")

# Extended unpacking
tuple_values = (1, 2, 3, 4, 5)
first, *middle, last = tuple_values
print("First:", first, "| Middle:", middle, "| Last:", last)

# ---------------------------
# 5. Nested Tuples
# ---------------------------
print("\n5. Nested Tuples")

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("Matrix[1][2]:", matrix[1][2])

# ---------------------------
# 6. Using Tuples as Dictionary Keys
# ---------------------------
print("\n6. Using Tuples as Dictionary Keys")

location_map = {
    (35.6895, 139.6917): "Tokyo",
    (34.6937, 135.5023): "Osaka"
}
print("City at (35.6895,139.6917):", location_map[(35.6895, 139.6917)])

# ---------------------------
# 7. Returning Multiple Values from a Function
# ---------------------------
print("\n7. Returning Multiple Values from a Function")

def min_and_max(values):
    return min(values), max(values)

nums = [5, 1, 9, 3]
mn, mx = min_and_max(nums)
print(f"Min: {mn}, Max: {mx}")
