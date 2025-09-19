"""
type_conversion_demo.py
Author: Sen SD
Description:
    Simple examples of Python type conversions:
    - float to int
    - int to float
    - int pair to complex
"""

# Convert float to int (truncates the decimal part, does NOT round)
print(int(3.9))       # 3

# Convert int to float
print(float(7))       # 7.0

# Create a complex number from two integers
print(complex(2, 3))  # (2+3j)

print(int(-4.8))      # -4  (truncates toward zero)
print(float("5.5"))   # 5.5 (string to float)