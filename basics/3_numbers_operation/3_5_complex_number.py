"""
complex_numbers.py
Author: Sen SD
Summary:
    Demonstrates Python complex number operations including:
    - Creation of complex numbers
    - Arithmetic operations
    - Conjugate and magnitude
    - Real and imaginary parts
    - Built-in functions with complex numbers
    - User input for complex numbers
"""

# ---------------------------
# 1. Complex Number Creation
# ---------------------------
print("1. Complex Number Creation")
c1 = complex(2, 3)
c2 = 1 - 4j
print("Input c1:", c1)
print("Input c2:", c2)
print()

# ---------------------------
# 2. Arithmetic Operations
# ---------------------------
print("2. Arithmetic Operations")
print("Addition: c1 + c2 =", c1 + c2)
print("Subtraction: c1 - c2 =", c1 - c2)
print("Multiplication: c1 * c2 =", c1 * c2)
print("Division: c1 / c2 =", c1 / c2)
print()

# ---------------------------
# 3. Conjugate & Magnitude
# ---------------------------
print("3. Conjugate & Magnitude")
print("Input c1:", c1)
print("Conjugate of c1:", c1.conjugate())
print("Magnitude (abs) of c1:", abs(c1))
print()

# ---------------------------
# 4. Real and Imaginary Parts
# ---------------------------
print("4. Real and Imaginary Parts")
print("Input c2:", c2)
print("Real part:", c2.real)
print("Imaginary part:", c2.imag)
print()

# ---------------------------
# 5. Built-in Functions with Complex Numbers
# ---------------------------
print("5. Built-in Functions")
print("Input c1:", c1)
print("Type:", type(c1))
print("Complex from tuple (3,4):", complex(3,4))
print()

# ---------------------------
# 6. Useful Tricks
# ---------------------------
print("6. Useful Tricks")
c3 = 5 + 0j
print("Input c3:", c3)
# Check if imaginary part is zero
print("Is real only?:", c3.imag == 0)
# Swap real and imaginary (demonstration)
swapped = complex(c3.imag, c3.real)
print("Swapped real/imag:", swapped)
print()

# ---------------------------
# 7. User Input
# ---------------------------
print("7. User Input")
real_input = input("Enter real part of complex number: ")
imag_input = input("Enter imaginary part of complex number: ")
print("Inputs: real =", real_input, ", imag =", imag_input)
try:
    c_user = complex(float(real_input), float(imag_input))
    print("Complex number:", c_user)
    print("Magnitude:", abs(c_user))
    print("Conjugate:", c_user.conjugate())
    print("Real part:", c_user.real)
    print("Imaginary part:", c_user.imag)
except ValueError:
    print("Invalid input! Please enter numeric values for real and imaginary parts.")
