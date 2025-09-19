"""
3_1_number_types.py
Author : Sen SD
Summary:
    Demonstrates Python number types with examples:
    - int, float, complex, bool
    - Shows their values and usage
"""

# ---------------------------
# Number Types Table
# ---------------------------
print("Python Number Types Table")
print("| Type    | Example                 | Notes                                                      |")
print("| ------- | ----------------------- | ---------------------------------------------------------- |")
print("| int     | 42, -7, 0               | Whole numbers of unlimited size (no explicit 'long' type). |")
print("| float   | 3.14, -0.001, 2.0       | Double-precision floating point.                           |")
print("| complex | 3 + 4j                  | Real and imaginary parts, where j is √-1.                |")
print("| bool    | True, False             | Subclass of int (True == 1, False == 0).                 |")
print()

# ---------------------------
# 1. Integer Examples
# ---------------------------
print("1. Integer Examples")
i1 = 42
i2 = -7
i3 = 0
print("Inputs:", i1, i2, i3)
print("Addition:", i1 + i2)
print("Multiplication:", i1 * i2)
print("Division (float):", i1 / 2)
print("Floor Division:", i1 // 2)
print("Modulo:", i1 % 5)
print()

# ---------------------------
# 2. Float Examples
# ---------------------------
print("2. Float Examples")
f1 = 3.14
f2 = -0.001
f3 = 2.0
print("Inputs:", f1, f2, f3)
print("Addition:", f1 + f2)
print("Multiplication:", f1 * f3)
print("Division:", f1 / f3)
print("Rounded f1:", round(f1))
print()

# ---------------------------
# 3. Complex Examples
# ---------------------------
print("3. Complex Examples")
c1 = 3 + 4j
c2 = 1 - 2j
print("Inputs:", c1, c2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)
print("Magnitude of c1:", abs(c1))
print("Conjugate of c1:", c1.conjugate())
print("Real part of c1:", c1.real)
print("Imag part of c1:", c1.imag)
print()

# ---------------------------
# 4. Boolean Examples
# ---------------------------
print("4. Boolean Examples")
b1 = True
b2 = False
print("Inputs:", b1, b2)
print("b1 + b2 =", b1 + b2)
print("b1 * 10 =", b1 * 10)
print("Not b1:", not b1)
print("b1 == 1:", b1 == 1)
print("b2 == 0:", b2 == 0)
print()
