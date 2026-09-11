# Python Practice - While Loops

# 1. Print 1 to N
n = int(input("Enter N: "))
i = 1
while i <= n:
    print(i)
    i += 1

# 2. Sum of digits
n = abs(int(input("Enter number: ")))
total = 0
while n:
    total += n % 10
    n //= 10
print("Digit sum:", total)

# 3. Palindrome number
n = int(input("Enter number: "))
original = abs(n)
reverse = 0
temp = original
while temp:
    reverse = reverse * 10 + temp % 10
    temp //= 10
print("Palindrome" if original == reverse else "Not palindrome")

# 4. Count even and odd digits
n = abs(int(input("Enter number: ")))
even = odd = 0
if n == 0: even = 1
while n:
    if (n % 10) % 2 == 0: even += 1
    else: odd += 1
    n //= 10
print("Even digits:", even, "Odd digits:", odd)

# 5. Largest digit
n = abs(int(input("Enter number: ")))
largest = 0
while n:
    largest = max(largest, n % 10)
    n //= 10
print("Largest digit:", largest)

# 6. Add numbers until 0
total = 0
while True:
    n = float(input("Enter number (0 to stop): "))
    if n == 0: break
    total += n
print("Total:", total)

# 7. Guess a secret number
secret = 7
while True:
    guess = int(input("Guess 1-10: "))
    if guess == secret:
        print("Correct!")
        break
    print("Too low" if guess < secret else "Too high")

# 8. Multiplication table
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1

# 9. Factorial
n = int(input("Enter non-negative number: "))
fact, i = 1, 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)

# 10. Skip multiples of 3
i = 1
while i <= 30:
    if i % 3 != 0: print(i)
    i += 1
