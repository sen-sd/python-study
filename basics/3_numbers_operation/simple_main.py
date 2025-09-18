print("Int Addition 2 + 2 = ",2 + 2) # Int Addition
print("Int Subtraction 5 - 2 = ",5 - 2) # Int Subtraction
print("division  8 / 5 = ", 8 / 5)  # → 1.6 - division always returns a floating-point number

# floor division
# In Python 3 the / operator always returns a floating-point result.
# If you want an integer result, use floor division // or an explicit conversion, depending on the behavior you need.
print("floor division 8 // 5 = ",8 // 5) # → 1, floor division discards the fractional part

# remainder
print("remainder 17 % 3 = ",17 % 3) # → 2, the % operator returns the remainder of the division

# squared
print("squared 5 ** 2 = ",5 ** 2) # → 25, 5 squared
print("squared 2 ** 7 = ",2 ** 7) # → 128, # 2 to the power of 7


# Use divmod to get integer quotient and remainder in one call:
quotient, remainder = divmod(8, 5)
print(f"Quotient: {quotient}, Remainder: {remainder}")

# If you just want to drop the decimal part (truncate), convert to int:
result = int(8 / 5)   # → 1
print(f"decimal part (truncate), convert to int:: {result}")
result = int(-8 / 5)  # → -1  (note: different from floor division)
print(f"decimal part (truncate), convert to int:: {result}")
