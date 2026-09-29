# 83 Common Design Patterns
# 1 Singleton
class Config:
 _x=None
 def __new__(cls):
  if cls._x is None: cls._x=super().__new__(cls)
  return cls._x
print("1",Config() is Config())
# 2 Factory
class Dog:
 def speak(self): return "Woof"
class Cat:
 def speak(self): return "Meow"
def factory(k): return Dog() if k=="dog" else Cat()
print("2",factory("dog").speak())
# 3 Strategy
class Add:
 def run(self,a,b): return a+b
class Mul:
 def run(self,a,b): return a*b
class Calculator:
 def __init__(self,s): self.s=s
 def run(self,a,b): return self.s.run(a,b)
print("3",Calculator(Add()).run(5,3),Calculator(Mul()).run(5,3))
# 4 Observer
class News:
 def __init__(self): self.obs=[]
 def subscribe(self,o): self.obs.append(o)
 def publish(self,x):
  for o in self.obs:o.update(x)
class User:
 def __init__(self,n): self.n=n
 def update(self,x): print("4",self.n,x)
n=News(); n.subscribe(User("Aman")); n.subscribe(User("Riya")); n.publish("News")
# 5 Adapter
class Legacy:
 def old(self,x): return "Legacy "+x
class Adapter:
 def __init__(self,x): self.x=x
 def print(self,x): return self.x.old(x)
print("5",Adapter(Legacy()).print("Hello"))
# 6 Decorator
class Coffee:
 def cost(self): return 50
class Milk:
 def __init__(self,x): self.x=x
 def cost(self): return self.x.cost()+20
print("6",Milk(Coffee()).cost())
# 7 Command
class Light:
 def on(self): return "ON"
class Command:
 def __init__(self,x): self.x=x
 def execute(self): return self.x.on()
print("7",Command(Light()).execute())
# 8 Builder
class Person:
 def __init__(self,n,a,c): self.n,self.a,self.c=n,a,c
 def __repr__(self): return f"{self.n}, {self.a}, {self.c}"
class Builder:
 def __init__(self): self.v=["",0,""]
 def name(self,x): self.v[0]=x; return self
 def age(self,x): self.v[1]=x; return self
 def city(self,x): self.v[2]=x; return self
 def build(self): return Person(*self.v)
print("8",Builder().name("Aman").age(22).city("Delhi").build())
# 9 Repository
class Repo:
 def __init__(self): self.d={}
 def add(self,k,v): self.d[k]=v
 def get(self,k): return self.d.get(k)
r=Repo(); r.add(1,"Python"); print("9",r.get(1))
# 10 Chain
class H:
 def __init__(self,n=None): self.n=n
 def handle(self,x): return self.n.handle(x) if self.n else "Unhandled"
class Pos(H):
 def handle(self,x): return "Positive" if x>0 else super().handle(x)
class Neg(H):
 def handle(self,x): return "Negative" if x<0 else super().handle(x)
print("10",Pos(Neg()).handle(-2))
# 11 Facade
class Inventory:
 def check(self): return "Checked"
class Payment:
 def pay(self): return "Paid"
class Shipping:
 def ship(self): return "Shipped"
class Order:
 def place(self): return [Inventory().check(),Payment().pay(),Shipping().ship()]
print("11",Order().place())
