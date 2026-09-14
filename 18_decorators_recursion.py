# Decorators and Recursion - 10 Programs
# 1. Basic decorator
def deco(f):
    def wrapper(): print("Before"); f(); print("After")
    return wrapper
@deco
def hello(): print("Hello Python")
hello()
# 2. Decorator with arguments
def greet_deco(f):
    def wrapper(name): print("Welcome"); f(name)
    return wrapper
@greet_deco
def greet(name): print("Hello",name)
greet(input("Name: "))
# 3. Recursive countdown
def countdown(n):
    if n==0:return
    print(n); countdown(n-1)
countdown(int(input("Countdown: ")))
# 4. Recursive factorial
def factorial(n): return 1 if n<=1 else n*factorial(n-1)
print(factorial(int(input("Factorial number: "))))
# 5. Recursive Fibonacci
def fib(n): return n if n<=1 else fib(n-1)+fib(n-2)
print(fib(int(input("Fibonacci position: "))))
# 6. Recursive natural sum
def total(n): return 0 if n==0 else n+total(n-1)
print(total(int(input("N: "))))
# 7. Recursive power
def power(a,b): return 1 if b==0 else a*power(a,b-1)
print(power(int(input("Base: ")),int(input("Exponent: "))))
# 8. Decorator returning result
def show(f):
    def wrapper(*args): print("Calling function"); return f(*args)
    return wrapper
@show
def add(a,b): return a+b
print(add(5,7))
# 9. Recursive digit sum
def digit_sum(n): return abs(n) if abs(n)<10 else abs(n)%10+digit_sum(abs(n)//10)
print(digit_sum(int(input("Number: "))))
# 10. Recursive string reverse
def reverse(s): return s if len(s)<=1 else reverse(s[1:])+s[0]
print(reverse(input("String: ")))
