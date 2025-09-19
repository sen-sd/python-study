"""
text_operations_demo.py
Author : Your Name
Date   : YYYY-MM-DD
Summary:
    Demonstrates Python text (string) operations including:
    - Creation, indexing, slicing
    - Case conversion
    - Stripping, padding
    - Searching and replacing
    - Splitting and joining
    - Content checks
    - Formatting strings
    - Escape characters, raw strings, and multi-line strings
    - Useful tricks (reversing, counting, swapping case, padding numbers)
    - User input
"""

# ---------------------------
# 1. String Creation
# ---------------------------
print("1. String Creation")
s1 = "Hello"
s2 = 'World'
s3 = """This is
a multi-line string"""
print("Input s1:", s1)
print("Input s2:", s2)
print("Input s3:", s3)
print()

# ---------------------------
# 2. Indexing & Slicing
# ---------------------------
print("2. Indexing & Slicing")
s = "Python"
print("Input:", s)
print("First char:", s[0])
print("Last char:", s[-1])
print("Slice [1:4]:", s[1:4])
print("Slice [::2]:", s[::2])
print()

# ---------------------------
# 3. Concatenation & Repetition
# ---------------------------
print("3. Concatenation & Repetition")
s1 = "Hello"
s2 = "World"
print("Inputs:", s1, s2)
print("Concatenation:", s1 + " " + s2)
print("Repetition:", "Ha" * 3)
print()

# ---------------------------
# 4. Length & Membership
# ---------------------------
print("4. Length & Membership")
s = "Python"
print("Input:", s)
print("Length:", len(s))
print("'y' in s:", 'y' in s)
print("'z' not in s:", 'z' not in s)
print()

# ---------------------------
# 5. Case Conversion
# ---------------------------
print("5. Case Conversion")
s = "python"
print("Input:", s)
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Title:", s.title())
print("Capitalize:", s.capitalize())
print()

# ---------------------------
# 6. Stripping & Padding
# ---------------------------
print("6. Stripping & Padding")
s = "   Hello   "
print("Input:", repr(s))
print("Strip:", s.strip())
print("Left strip:", s.lstrip())
print("Right strip:", s.rstrip())
print("Center padded:", s.strip().center(10, "*"))
print()

# ---------------------------
# 7. Searching & Replacing
# ---------------------------
print("7. Searching & Replacing")
s = "Hello World"
print("Input:", s)
print("Find 'World':", s.find("World"))
print("Replace 'World' with 'Python':", s.replace("World", "Python"))
print()

# ---------------------------
# 8. Splitting & Joining
# ---------------------------
print("8. Splitting & Joining")
s = "Python,Java,C++"
print("Input:", s)
parts = s.split(",")
print("Split:", parts)
joined = " | ".join(parts)
print("Joined:", joined)
print()

# ---------------------------
# 9. Checking String Content
# ---------------------------
print("9. Checking String Content")
s = "123"
print("Input:", s)
print("isdigit():", s.isdigit())
print("isalpha():", s.isalpha())
print("isalnum():", s.isalnum())
print("isspace():", " ".isspace())
print()

# ---------------------------
# 10. String Formatting
# ---------------------------
print("10. String Formatting")
name = "Alice"
age = 25
pi = 3.14159
print("Inputs: name =", name, ", age =", age, ", pi =", pi)
print("Old-style: Name: %s, Age: %d" % (name, age))
print("str.format(): Name: {}, Age: {}".format(name, age))
print(f"f-string: Name: {name}, Age: {age}")
print(f"Pi rounded: {pi:.2f}")
print()

# ---------------------------
# 11. Escape Characters
# ---------------------------
print("11. Escape Characters")
s_newline = "Line1\nLine2"
s_tab = "Tab\tIndented"
s_backslash = "\\"
s_quotes = "'single', \"double\""
print("Input examples:")
print("Newline input:", repr(s_newline))
print("Tab input:", repr(s_tab))
print("Backslash input:", repr(s_backslash))
print("Quotes input:", repr(s_quotes))
print("Outputs:")
print(s_newline)
print(s_tab)
print(s_backslash)
print(s_quotes)
print()

# ---------------------------
# 12. Raw Strings
# ---------------------------
print("12. Raw Strings")
path = r"C:\Users\Name\Desktop"
print("Input:", path)
print("Raw string path:", path)
print()

# ---------------------------
# 13. Multi-line Strings / Docstrings
# ---------------------------
print("13. Multi-line Strings / Docstrings")
def example_func():
    """
    Example function showing a multi-line docstring.
    Returns a greeting string.
    """
    return "Hello from function"

print("Function output:", example_func())
print("Function docstring:", example_func.__doc__)
print()

# ---------------------------
# 14. Useful Tricks
# ---------------------------
print("14. Useful Tricks")
s = "Python"
print("Input:", s)
print("Reversed:", s[::-1])

s2 = "hello world"
print("Input:", s2)
print("Count 'l':", s2.count("l"))
print("Starts with 'he':", s2.startswith("he"))
print("Ends with 'ld':", s2.endswith("ld"))
print("Swap case:", "Hello World".swapcase())

num = 1234567
print("Input number:", num)
print("Formatted number:", f"{num:,}")
print("Padded number:", f"{42:05}")
print()

# ---------------------------
# 15. User Input
# ---------------------------
print("15. User Input")
# String input
name = input("Enter your name: ")
print("Input:", name)
print(f"Hello, {name}!")

# Integer input
age_input = input("Enter your age: ")
print("Input:", age_input)
try:
    age = int(age_input)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid input! Please enter a number.")

# Float input
height_input = input("Enter your height in meters (e.g., 1.75): ")
print("Input:", height_input)
try:
    height = float(height_input)
    print(f"Your height is {height} m.")
except ValueError:
    print("Invalid input! Please enter a valid float number.")
