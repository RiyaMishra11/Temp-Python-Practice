"""File 74: Type Hints and Protocols | 11 Programs"""
from typing import Protocol,TypeVar,Generic,Callable,Optional

def program_1():
    def add(a:int,b:int)->int:return a+b
    print(add(10,20))

def program_2():
    names:list[str]=["Aman","Riya"]; scores:dict[str,int]={"Aman":85}
    print(names,scores)

def program_3():
    def find(names:list[str],target:str)->Optional[str]:
        return target if target in names else None
    print(find(["Aman","Riya"],"Riya")); print(find(["Aman"],"Kabir"))

def program_4():
    def calc(a:int,b:int,op:Callable[[int,int],int])->int:return op(a,b)
    print(calc(10,5,lambda x,y:x+y)); print(calc(10,5,lambda x,y:x*y))

T=TypeVar("T")
def first(items:list[T])->T:return items[0]

def program_5():
    print(first([10,20])); print(first(["Python","Java"]))

class Box(Generic[T]):
    def __init__(self,value:T):self.value=value
    def get(self)->T:return self.value

def program_6():
    print(Box(100).get()); print(Box("Hello").get())

class Printable(Protocol):
    def display(self)->str:...

class User:
    def __init__(self,name:str):self.name=name
    def display(self)->str:return "User: "+self.name

def show(x:Printable):print(x.display())

def program_7():show(User("Aman"))

def program_8():
    UserRecord=dict[str,str|int]
    user:UserRecord={"name":"Riya","age":22}; print(user)

def program_9():
    products:list[dict[str,str|int]]=[{"name":"Laptop","price":65000},{"name":"Mouse","price":1200}]
    print([p for p in products if int(p["price"])>2000])

class Stack(Generic[T]):
    def __init__(self):self.items:list[T]=[]
    def push(self,x:T)->None:self.items.append(x)
    def pop(self)->T:return self.items.pop()

def program_10():
    s=Stack[int]()
    for x in [10,20,30]:s.push(x)
    print(s.pop(),s.pop())

def program_11():
    Op=Callable[[float,float],float]
    ops:dict[str,Op]={"add":lambda a,b:a+b,"sub":lambda a,b:a-b,"mul":lambda a,b:a*b,"div":lambda a,b:a/b if b else 0}
    print(ops["mul"](12,5))

if __name__=="__main__":program_1()
