# Python Practice - Conditionals

# 1. Check voting eligibility
age = int(input("Enter your age: "))
print("Eligible to vote" if age >= 18 else "Not eligible to vote")

# 2. Greatest of three numbers
a, b, c = map(float, input("Enter three numbers: ").split())
print("Greatest:", max(a, b, c))

# 3. Calculate grade
marks = float(input("Enter marks: "))
if marks >= 90: grade = "A+"
elif marks >= 80: grade = "A"
elif marks >= 70: grade = "B"
elif marks >= 60: grade = "C"
elif marks >= 50: grade = "D"
else: grade = "F"
print("Grade:", grade)

# 4. Check leap year
year = int(input("Enter year: "))
print("Leap year" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "Not a leap year")

# 5. Divisible by 5 and 11
n = int(input("Enter number: "))
print("Divisible by both" if n % 5 == 0 and n % 11 == 0 else "Not divisible by both")

# 6. Classify triangle
a, b, c = map(float, input("Enter three sides: ").split())
if a + b <= c or a + c <= b or b + c <= a: print("Invalid triangle")
elif a == b == c: print("Equilateral")
elif a == b or b == c or a == c: print("Isosceles")
else: print("Scalene")

# 7. Electricity bill
units = float(input("Enter units: "))
if units <= 100: bill = units * 1.5
elif units <= 200: bill = 150 + (units - 100) * 2.5
elif units <= 300: bill = 400 + (units - 200) * 4
else: bill = 800 + (units - 300) * 6
print("Bill:", bill)

# 8. Admission eligibility
marks = float(input("Enter percentage: "))
attendance = float(input("Enter attendance percentage: "))
print("Eligible" if marks >= 60 and attendance >= 75 else "Not eligible")

# 9. Simple calculator
a, b = map(float, input("Enter two numbers: ").split())
op = input("Enter operator (+,-,*,/): ")
if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/": print("Cannot divide by zero" if b == 0 else a / b)
else: print("Invalid operator")

# 10. Determine point quadrant
x, y = map(float, input("Enter x and y: ").split())
if x == 0 and y == 0: print("Origin")
elif x == 0: print("Y-axis")
elif y == 0: print("X-axis")
elif x > 0 and y > 0: print("First quadrant")
elif x < 0 and y > 0: print("Second quadrant")
elif x < 0 and y < 0: print("Third quadrant")
else: print("Fourth quadrant")
