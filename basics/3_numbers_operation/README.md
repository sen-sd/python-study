Python Study Demos
==================

This repository contains Python study/demo files covering numbers, arithmetic, numeric functions, type conversion, and complex numbers. Each file demonstrates key concepts with examples, input prints, and useful tricks.

------------------------------------------------------------
File List
------------------------------------------------------------

1. 3_1_number_types.py
   Purpose: Demonstrates different numeric types in Python.
   Highlights:
     - Integer, Float, and Complex numbers
     - Variable assignments and printing
     - Examples showing type differences
   Example:
     i = 10
     f = 3.5
     c = 2 + 3j
     print("Integer:", i)
     print("Float:", f)
     print("Complex:", c)

2. 3_2_basic_arithmetic.py
   Purpose: Shows basic arithmetic operations in Python.
   Highlights:
     - Addition, Subtraction, Multiplication, Division
     - Floor division and modulo
     - Exponentiation
     - Swapping numbers
     - Using divmod for quotient and remainder
   Example:
     a, b = 8, 5
     print("Addition:", a + b)
     print("Division (float):", a / b)
     q, r = divmod(a, b)
     print("Quotient:", q, "Remainder:", r)

3. 3_3_numeric_functions.py
   Purpose: Demonstrates Python built-in numeric functions.
   Highlights:
     - abs(), round(), pow()
     - Checking even/odd numbers
     - Binary, Hex, and Octal conversions
     - Useful numeric tricks
   Example:
     n = -5
     f = 3.7
     print("Absolute:", abs(n))
     print("Round:", round(f))
     print("Power:", pow(2,3))

4. 3_4_type_conversion.py
   Purpose: Shows type conversion between numeric types.
   Highlights:
     - Converting float to int
     - Converting int to float
     - Creating complex numbers
     - Safe type conversion examples
   Example:
     f1 = 3.9
     i1 = int(f1)
     f2 = float(7)
     c1 = complex(2,3)
     print("Float to int:", i1)
     print("Int to float:", f2)
     print("Complex number:", c1)

5. 3_5_complex_number.py
   Purpose: Demonstrates complex number operations in Python.
   Highlights:
     - Creating complex numbers
     - Arithmetic operations (+, -, *, /)
     - Conjugate, magnitude, real and imaginary parts
     - User input for complex numbers
     - Useful tricks with complex numbers
   Example:
     c1 = complex(2,3)
     c2 = 1-4j
     print("Addition:", c1 + c2)
     print("Magnitude of c1:", abs(c1))
     print("Conjugate of c2:", c2.conjugate())
