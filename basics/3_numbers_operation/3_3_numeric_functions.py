"""
numeric_functions.py
Author : Sen SD
Description:
    Examples of Python numeric functions:
    - Built-in functions
    - math module functions
    - usage
    -   python 3_3_numeric_functions.py
"""


# -----------------------------
# Built-in numeric functions
# For Built-in numeric functions no need any Import
# -----------------------------
print("=== Built-in numeric functions ===")

x = -7
print("abs(-7)         ->", abs(x))             # 7  (absolute value)

numbers = [2, 5, 1, 9, 4]
print("min(numbers)    ->", min(numbers))       # 1  (smallest)
print("max(numbers)    ->", max(numbers))       # 9  (largest)
print("sum(numbers)    ->", sum(numbers))       # 21 (total)

print("round(3.14159, 2) ->", round(3.14159, 2)) # 3.14 (round to 2 decimals)
print("pow(2, 3)         ->", pow(2, 3))         # 8   (2**3)

# divmod returns quotient and remainder together
q, r = divmod(17, 4)
print("divmod(17, 4)   -> quotient:", q, ", remainder:", r)  # 4, 1

# -----------------------------
# math module functions
# -----------------------------
import math

print("\n=== math module functions ===")

print("math.sqrt(16)   ->", math.sqrt(16))      # 4.0
print("math.ceil(2.3)  ->", math.ceil(2.3))     # 3   (round up)
print("math.floor(2.7) ->", math.floor(2.7))    # 2   (round down)
print("math.factorial(5)->", math.factorial(5)) # 120
print("math.pi         ->", math.pi)           # 3.141592653589793
print("math.e          ->", math.e)            # 2.718281828459045
print("math.gcd(24,36) ->", math.gcd(24,36))   # 12  (greatest common divisor)
print("math.lcm(4,6)   ->", math.lcm(4,6))     # 12  (least common multiple)

# Trigonometric example
angle = math.radians(30)  # convert 30° to radians
print("math.sin(30°)   ->", math.sin(angle))   # 0.499999... ≈ 0.5
print("math.cos(30°)   ->", math.cos(angle))   # 0.8660...

# Logarithms
print("math.log(100, 10) ->", math.log(100, 10)) # 2.0
print("math.log10(1000)  ->", math.log10(1000))  # 3.0