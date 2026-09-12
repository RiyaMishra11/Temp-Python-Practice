# Python Practice - Modules
import math, random, statistics
from datetime import date

# 1. Square root
n=float(input("Number: ")); print(math.sqrt(n))

# 2. Factorial
n=int(input("Number: ")); print(math.factorial(n))

# 3. GCD and LCM
a,b=map(int,input("Two numbers: ").split()); print(math.gcd(a,b), math.lcm(a,b))

# 4. Random number
print("Random:", random.randint(1,100))

# 5. Random password
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
print("Password:", "".join(random.choice(chars) for _ in range(8)))

# 6. Current date
print("Today:", date.today())

# 7. Days between dates
d1=date(2026,1,1); d2=date(2026,9,2); print((d2-d1).days)

# 8. Mean and median
nums=list(map(float,input("Numbers: ").split()))
print("Mean:",statistics.mean(nums)); print("Median:",statistics.median(nums))

# 9. Power
a,b=map(float,input("Base and exponent: ").split()); print(math.pow(a,b))

# 10. Degrees to radians
deg=float(input("Degrees: ")); print(math.radians(deg))
