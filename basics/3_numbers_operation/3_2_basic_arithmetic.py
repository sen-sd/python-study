# | Operator | Example  | Result                                 |
# | -------- | -------- | -------------------------------------- |
# | `+`      | `5 + 2`  | `7`                                    |
# | `-`      | `5 - 2`  | `3`                                    |
# | `*`      | `5 * 2`  | `10`                                   |
# | `/`      | `5 / 2`  | `2.5` (always float)                   |
# | `//`     | `5 // 2` | `2` (floor division, integer quotient) |
# | `%`      | `5 % 2`  | `1` (remainder)                        |
# | `**`     | `5 ** 2` | `25` (power)                           |


"""
number_operations_demo.py
Author : Sen SD
Summary:
    Demonstrates Python numeric operations including:
    - Integer, float, complex numbers
    - Arithmetic operations
    - Type conversions
    - Built-in numeric functions
    - divmod usage
    - Useful tricks
    - User input
"""

# ---------------------------
# 1. Integer, Float, Complex
# ---------------------------
print("1. Integer, Float, Complex")
i = 10
f = 3.5
c = 2 + 3j
print("Input integer:", i)
print("Input float:", f)
print("Input complex:", c)
print()

# ---------------------------
# 2. Arithmetic Operations
# ---------------------------
print("2. Arithmetic Operations")
a, b = 8, 5
print("Inputs: a =", a, ", b =", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division (float):", a / b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Exponent:", a ** b)
print()

# ---------------------------
# 3. Swapping Numbers
# ---------------------------
print("3. Swapping Numbers")
a, b = 5, 10
print("Input: a =", a, ", b =", b)
a, b = b, a
print("After swap: a =", a, ", b =", b)
print()

# ---------------------------
# 4. Type Conversion
# ---------------------------
print("4. Type Conversion")
f1 = 3.9
i1 = int(f1)
f2 = float(7)
c1 = complex(2, 3)
print("Input float:", f1, "-> int:", i1)
print("Input int:", 7, "-> float:", f2)
print("Complex(2,3):", c1)
print()

# ---------------------------
# 5. divmod Function
# ---------------------------
print("5. divmod Function")
x, y = 8, 5
print("Inputs: x =", x, ", y =", y)
q, r = divmod(x, y)
print("Quotient:", q)
print("Remainder:", r)
print()

# ---------------------------
# 6. Built-in Numeric Functions
# ---------------------------
print("6. Built-in Numeric Functions")
n = -5
f = 3.7
print("Input integer:", n)
print("abs():", abs(n))
print("Input float:", f)
print("round():", round(f))
print("floor():", int(f))  # basic integer conversion as floor
print("pow(2,3):", pow(2,3))
print()

# ---------------------------
# 7. Complex Number Operations
# ---------------------------
print("7. Complex Number Operations")
c1 = 2 + 3j
c2 = 1 - 4j
print("Inputs: c1 =", c1, ", c2 =", c2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)
print("Absolute (magnitude) of c1:", abs(c1))
print("Conjugate of c1:", c1.conjugate())
print()

# ---------------------------
# 8. Useful Tricks
# ---------------------------
print("8. Useful Tricks")
num = 15
print("Input number:", num)
print("Check even:", num % 2 == 0)
print("Check odd:", num % 2 != 0)
print("Binary:", bin(num))
print("Hex:", hex(num))
print("Octal:", oct(num))
print()

# ---------------------------
# 9. User Input
# ---------------------------
print("9. User Input")
# Integer input
num_input = input("Enter an integer: ")
print("Input:", num_input)
try:
    num_int = int(num_input)
    print("You entered integer:", num_int)
except ValueError:
    print("Invalid integer input!")

# Float input
flt_input = input("Enter a float: ")
print("Input:", flt_input)
try:
    num_float = float(flt_input)
    print("You entered float:", num_float)
except ValueError:
    print("Invalid float input!")

# Complex input
comp_input_real = input("Enter complex real part: ")
comp_input_imag = input("Enter complex imaginary part: ")
print("Inputs: real =", comp_input_real, ", imag =", comp_input_imag)
try:
    c = complex(float(comp_input_real), float(comp_input_imag))
    print("Complex number:", c)
except ValueError:
    print("Invalid complex input!")


