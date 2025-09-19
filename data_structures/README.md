Data Structures - Python Study
==============================

This folder contains Python demos and implementations for both **built-in collections** and **classic data structures**.  
It is designed for study and practice, with examples and useful tricks.

------------------------------------------------------------
Folder Structure
------------------------------------------------------------
```
data_structures/
├── list_demo.py
├── tuple_demo.py
├── set_demo.py
├── dictionary_demo.py
├── stack.py
├── queue.py
├── linked_list.py
└── expandable/
    ├── tree.py
    ├── graph.py
    ├── heap.py
    └── sorting_algorithms.py
```

------------------------------------------------------------
Files Description
------------------------------------------------------------

1. list_demo.py
   - Demonstrates Python built-in list operations
   - Examples: indexing, slicing, append/remove, iteration, length
   - Useful for understanding mutable ordered sequences

2. tuple_demo.py
   - Demonstrates Python built-in tuple operations
   - Examples: indexing, slicing, immutability
   - Useful for fixed ordered sequences

3. set_demo.py
   - Demonstrates Python built-in set operations
   - Examples: add/remove, membership check, union, intersection, difference
   - Useful for unique unordered elements

4. dictionary_demo.py
   - Demonstrates Python built-in dictionary operations
   - Examples: access, add/update/delete, keys/values, iteration
   - Useful for key-value mappings

5. stack.py
   - Implementation of a Stack (LIFO) data structure
   - Methods: push, pop, peek, is_empty
   - Can be implemented using list or class

6. queue.py
   - Implementation of a Queue (FIFO) data structure
   - Methods: enqueue, dequeue, peek, is_empty
   - Can be implemented using list or collections.deque

7. linked_list.py
   - Implementation of a simple singly linked list
   - Methods: add_node, remove_node, traversal
   - Useful to understand dynamic memory structures

8. expandable/
   - tree.py: Binary tree, Binary Search Tree (BST), traversal examples
   - graph.py: Graph representations, BFS, DFS
   - heap.py: Min-heap and Max-heap implementation
   - sorting_algorithms.py: Common sorting algorithms (bubble, selection, insertion, quicksort, mergesort)

------------------------------------------------------------
Notes
------------------------------------------------------------
- All files include **input prints** to demonstrate operations and outputs.
- `expandable/` folder is for future advanced topics and algorithms.
- File names use `_demo.py` suffix to avoid conflict with Python built-in types.
- These scripts are **ready for experimentation and practice**.