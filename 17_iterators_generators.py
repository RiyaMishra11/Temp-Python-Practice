# Iterators and Generators - 10 Programs
# 1. Create an iterator
items=[10,20,30,40]; it=iter(items); print(next(it)); print(next(it))
# 2. Iterate through a string
for ch in iter(input("Enter text: ")): print(ch)
# 3. Number generator
def numbers(n):
    for i in range(1,n+1): yield i
print(list(numbers(int(input("N: ")))))
# 4. Even generator
def evens(n):
    for i in range(2,n+1,2): yield i
print(list(evens(int(input("Limit: ")))))
# 5. Square generator
def squares(n):
    for i in range(1,n+1): yield i*i
print(list(squares(int(input("Terms: ")))))
# 6. Fibonacci generator
def fib(n):
    a,b=0,1
    for _ in range(n): yield a; a,b=b,a+b
print(list(fib(int(input("Fibonacci terms: ")))))
# 7. Positive-number generator
def positive(nums):
    for x in nums:
        if x>0: yield x
print(list(positive(map(int,input("Numbers: ").split()))))
# 8. Generator expression
g=(x*x for x in range(1,6)); print(list(g))
# 9. Countdown generator
def countdown(n):
    while n>0: yield n; n-=1
print(list(countdown(int(input("Countdown: ")))))
# 10. Multiples generator
def multiples(x,n):
    for i in range(1,n+1): yield x*i
print(list(multiples(int(input("Number: ")),int(input("Count: ")))))
