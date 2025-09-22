"""
set_demo.py
-----------
Demonstrates Python set operations.

Python Set:
- A set is an **unordered collection of unique elements**.
- Elements must be **hashable** (immutable types like numbers, strings, tuples).
- Sets do not allow duplicates.
- Sets are mutable (except frozensets) and support **set algebra operations**.
- Common use cases: removing duplicates, membership tests, mathematical operations on collections.

This demo covers:
- Creating sets (including empty and mixed-type sets)
- Adding and removing elements
- Checking membership
- Performing set algebra (union, intersection, difference, symmetric difference)
- Iterating over sets
- Set comprehensions
- Using frozen sets (immutable sets)
"""


# ---------------------------
# 1. Creating Sets
# ---------------------------
print("1. Creating Sets")

# A set automatically removes duplicates
numbers = {2, 1, 2, 3, 1}
print("Numbers set (duplicates removed):", numbers)

sort_data = {4, 2, 9, 1}
print("Without sort data", sort_data)          # order not guaranteed
print("After sort data", sorted(sort_data))  # Always [1, 2, 4, 9] # Sorted : convert to list

# Empty set: must use set() — {} creates a dict
empty_set = set()
print("Empty set:", empty_set)

# Mixed-type set
mixed = {42, "apple", 3.14, True}
print("Mixed-type set:", mixed)


# ---------------------------
# 2. Adding & Removing Elements
# ---------------------------
print("\n2. Adding & Removing Elements")

numbers.add(4)
print("After add(4):", numbers)

numbers.update([5, 6])
print("After update([5,6]):", numbers) # Update is called when need to add multiple elements.

numbers.discard(2)    # remove if present, no error if not
print("After discard(2):", numbers)

try:
    numbers.remove(99)  # remove raises KeyError if not present
except KeyError as e:
    print("Attempt to remove missing element:", e)

# ---------------------------
# 3. Membership Test
# ---------------------------
print("\n3. Membership Test")

print("Is 3 in numbers?", 3 in numbers)
print("Is 10 in numbers?", 10 in numbers)

# ---------------------------
# 4. Set Algebra
# ---------------------------
print("\n4. Set Algebra")

a = {1, 2, 3}
b = {3, 4, 5}

print("Union a|b:", a | b)
print("Intersection a&b:", a & b)
print("Difference a-b:", a - b)
print("Symmetric difference a^b:", a ^ b)

# ---------------------------
# 5. Iterating
# ---------------------------
print("\n5. Iterating")

for item in numbers:
    print("Item:", item)

# ---------------------------
# 6. Set Comprehension
# ---------------------------
print("\n6. Set Comprehension")

squares = {x * x for x in range(5)}
print("Squares set:", squares)

# ---------------------------
# 7. Frozen Set (Immutable)
# ---------------------------
print("\n7. Frozen Set (Immutable)")

frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)
# frozen.add(4)  # would raise AttributeError
