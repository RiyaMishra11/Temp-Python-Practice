# Python Practice - Comprehensions and Lambda

# 1. Squares
nums=range(1,11); print([n*n for n in nums])

# 2. Even numbers
nums=range(1,21); print([n for n in nums if n%2==0])

# 3. Uppercase words
words=input("Words: ").split(); print([w.upper() for w in words])

# 4. Long words
words=input("Words: ").split(); print([w for w in words if len(w)>5])

# 5. Lambda addition
a,b=map(float,input("Two numbers: ").split()); add=lambda x,y:x+y; print(add(a,b))

# 6. Lambda square
n=float(input("Number: ")); square=lambda x:x*x; print(square(n))

# 7. Sort words by length
words=input("Words: ").split(); print(sorted(words,key=lambda x:len(x)))

# 8. Dictionary comprehension
print({n:n**3 for n in range(1,6)})

# 9. Celsius to Fahrenheit
c=list(map(float,input("Celsius values: ").split())); print([(x*9/5)+32 for x in c])

# 10. Filter positive numbers
nums=list(map(int,input("Numbers: ").split())); print(list(filter(lambda x:x>0,nums)))
