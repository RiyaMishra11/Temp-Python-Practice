# 84 Performance & Optimization
import time
from functools import lru_cache
# 1 Timer
s=time.perf_counter(); sum(range(1000000)); print("1",round(time.perf_counter()-s,6))
# 2 Generator
g=(x*x for x in range(1000000)); print("2",[next(g) for _ in range(3)])
# 3 Comprehension
r=[x*2 for x in range(100000)]; print("3",len(r))
# 4 Set lookup
st=set(range(100000)); print("4",99999 in st)
# 5 Manual cache
cache={}
def calc(x):
 if x not in cache: cache[x]=x*x+10
 return cache[x]
print("5",calc(50),calc(50))
# 6 lru_cache
@lru_cache(maxsize=None)
def fib(n): return n if n<2 else fib(n-1)+fib(n-2)
print("6",fib(30),fib.cache_info())
# 7 Join
print("7"," ".join(["Python","is","fast"]))
# 8 Enumerate
for i,x in enumerate(["a","b","c"]): print("8",i,x)
# 9 Dict comprehension
print("9",{x:x*x for x in range(5)})
# 10 Chunks
def chunks(a,n):
 for i in range(0,len(a),n): yield a[i:i+n]
print("10",list(chunks(list(range(10)),3)))
# 11 Benchmark helper
def bench(fn,*args):
 t=[]
 for _ in range(5):
  s=time.perf_counter(); fn(*args); t.append(time.perf_counter()-s)
 return min(t)
def work(n): return sum(i*i for i in range(n))
print("11",round(bench(work,100000),6))
