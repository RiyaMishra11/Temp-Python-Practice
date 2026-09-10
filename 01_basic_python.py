# Basic Python Programs
# 1. Print Hello World
print("Hello, World!")

# 2. Take name as input and greet the user
name = input("Enter your name: ")
print("Hello,", name)

# 3. Add two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)

# 4. Find the area of a circle
radius = float(input("Enter radius: "))
area = 3.14159 * radius * radius
print("Area of circle:", area)

# 5. Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 6. Check whether a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 7. Find the largest of two numbers
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Largest:", max(x, y))

# 8. Check whether a number is positive, negative, or zero
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 9. Calculate simple interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
time = float(input("Enter time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

# 10. Swap two numbers
a = input("Enter first value: ")
b = input("Enter second value: ")
a, b = b, a
print("After swapping:")
print("First value:", a)
print("Second value:", b)
