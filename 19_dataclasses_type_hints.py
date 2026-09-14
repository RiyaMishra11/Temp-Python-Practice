# Dataclasses and Type Hints - 10 Programs
from dataclasses import dataclass,field
from typing import List,Dict,Optional
# 1. Basic dataclass
@dataclass
class Student: name:str; age:int
print(Student("Aman",20))
# 2. Product dataclass
@dataclass
class Product: name:str; price:float; quantity:int
p=Product("Keyboard",1200,2); print(p,p.price*p.quantity)
# 3. Typed addition
def add(a:float,b:float)->float:return a+b
print(add(10.5,20.5))
# 4. Typed average
def average(nums:List[float])->float:return sum(nums)/len(nums)
print(average([10,20,30]))
# 5. Default field
@dataclass
class Employee: name:str; department:str="General"
print(Employee("Riya"))
# 6. Dataclass method
@dataclass
class Rectangle:
    length:float; width:float
    def area(self)->float:return self.length*self.width
print(Rectangle(10,5).area())
# 7. Optional return
def find(names:List[str],target:str)->Optional[str]:
    for n in names:
        if n.lower()==target.lower():return n
    return None
print(find(["Aman","Riya"],input("Search name: ")))
# 8. Typed dictionary
def marks_total(marks:Dict[str,int])->int:return sum(marks.values())
print(marks_total({"Aman":80,"Riya":92}))
# 9. Dataclass list field
@dataclass
class Team: name:str; members:List[str]=field(default_factory=list)
t=Team("Python"); t.members+=["Aman","Riya"]; print(t)
# 10. Dataclass comparison
@dataclass
class Book: title:str; author:str
print(Book("Python","Author")==Book("Python","Author"))
