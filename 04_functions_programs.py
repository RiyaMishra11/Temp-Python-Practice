# Python Functions and Practical Programs

# 1. Function to add two numbers
def add(a, b):
    return a + b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", add(a, b))


# 2. Function to check even or odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

number = int(input("Enter a number: "))
print(even_or_odd(number))


# 3. Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))


# 4. Function to check prime number
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
print("Prime" if is_prime(number) else "Not Prime")


# 5. Function to find the maximum of three numbers
def maximum(a, b, c):
    return max(a, b, c)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Maximum:", maximum(a, b, c))


# 6. Function to calculate compound interest
def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount - principal

p = float(input("Enter principal amount: "))
r = float(input("Enter annual rate: "))
t = float(input("Enter time in years: "))
print("Compound Interest:", compound_interest(p, r, t))


# 7. Generate Fibonacci series
def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter number of terms: "))
print("Fibonacci series:", fibonacci(n))


# 8. Check whether a number is an Armstrong number
def is_armstrong(number):
    if number < 0:
        return False
    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == number

number = int(input("Enter a number: "))
print("Armstrong number" if is_armstrong(number) else "Not an Armstrong number")


# 9. Find the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))


# 10. Simple calculator using functions
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return "Cannot divide by zero" if b == 0 else a / b
    return "Invalid operator"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
print("Result:", calculator(a, b, operator))
