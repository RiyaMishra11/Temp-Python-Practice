# 63 Iterators, Generators and Context Managers - 11 programs
nums=iter([10,20,30])
print("1 Iterator:",next(nums),next(nums))
it=iter([1,2,3]);out=[]
try:
    while True: out.append(next(it))
except StopIteration: pass
print("2 Manual iteration:",out)
class Countdown:
    def __init__(self,n): self.n=n
    def __iter__(self): return self
    def __next__(self):
        if self.n==0: raise StopIteration
        x=self.n;self.n-=1;return x
print("3 Countdown:",list(Countdown(5)))
print("4 Generator expression:",list(x*x for x in range(5)))
def evens(n):
    for x in range(2,n+1,2): yield x
print("5 Generator:",list(evens(10)))
def numbers(n):
    for x in range(1,n+1): yield x
print("6 Pipeline:",list(x*x for x in numbers(5) if x%2))
p="/mnt/data/context_demo.txt"
with open(p,"w",encoding="utf-8") as f:f.write("Hello context manager")
with open(p,encoding="utf-8") as f:print("7 File:",f.read())
class Resource:
    def __enter__(self): print("8 Open"); return self
    def __exit__(self,*args): print("8 Close")
with Resource(): print("8 Inside")
from contextlib import contextmanager
@contextmanager
def message(msg):
    print("9 Start",msg)
    try: yield
    finally: print("9 End",msg)
with message("work"): print("9 Working")
def fib(n):
    a,b=0,1
    for _ in range(n): yield a; a,b=b,a+b
print("10 Fibonacci:",list(fib(8)))
def counter():
    n=1
    while True: yield n;n+=1
g=counter()
print("11 First five:",[next(g) for _ in range(5)])
