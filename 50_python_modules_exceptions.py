# Day 13 - 50: Modules, Exceptions and Robust Python
# 10 practical programs

import math
import random
from datetime import datetime

# 1. Square root using math
print("1. Square root:", math.sqrt(144))

# 2. Greatest common divisor
print("2. GCD:", math.gcd(48, 18))

# 3. Generate random number
print("3. Random number:", random.randint(1, 100))

# 4. Random choice
colors = ["red", "blue", "green", "yellow"]
print("4. Random choice:", random.choice(colors))

# 5. Safe integer conversion
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

print("5. Safe conversion:", safe_int("123"))
print("   Invalid conversion:", safe_int("abc"))

# 6. Division with exception handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print("6. Divide:", safe_divide(10, 2))
print("   Zero:", safe_divide(10, 0))

# 7. Validate positive number
def positive_number(value):
    if value <= 0:
        raise ValueError("Number must be positive")
    return value

try:
    print("7.", positive_number(25))
except ValueError as error:
    print("7. Error:", error)

# 8. Custom exception
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    return balance - amount

try:
    print("8. Balance:", withdraw(1000, 300))
except InsufficientBalanceError as error:
    print("8. Error:", error)

# 9. Finally block
def read_demo():
    try:
        return 10 / 2
    except Exception as error:
        return str(error)
    finally:
        print("9. Finally block executed")

print("9. Result:", read_demo())

# 10. Current timestamp
print("10. Timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
