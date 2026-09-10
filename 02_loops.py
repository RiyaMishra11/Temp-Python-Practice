# Python Loop Programs

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 1 to 50
for i in range(2, 51, 2):
    print(i)

# 3. Print odd numbers from 1 to 50
for i in range(1, 51, 2):
    print(i)

# 4. Find the sum of first N natural numbers
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)

# 5. Print multiplication table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 6. Find factorial of a number
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial:", factorial)

# 7. Count the digits of a number
n = abs(int(input("Enter a number: ")))
if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n //= 10
print("Number of digits:", count)

# 8. Reverse a number
n = int(input("Enter a number: "))
sign = -1 if n < 0 else 1
n = abs(n)
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print("Reversed number:", sign * reverse)

# 9. Check whether a number is prime
n = int(input("Enter a number: "))
is_prime = n >= 2
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print("Prime number" if is_prime else "Not a prime number")

# 10. Print a right-angle star pattern
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)
