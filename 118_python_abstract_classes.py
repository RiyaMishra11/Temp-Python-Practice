# 118 Abstract Classes
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self): pass
class Dog(Animal):
    def sound(self): return "Woof"
print("1.", Dog().sound())

class Shape(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass
class Square(Shape):
    def __init__(self, side): self.side=side
    def area(self): return self.side**2
    def perimeter(self): return 4*self.side
s=Square(5)
print("2.", s.area(), s.perimeter())

class Cat(Animal):
    def sound(self): return "Meow"
print("3.", [x.sound() for x in [Dog(),Cat()]])

class Vehicle(ABC):
    def start(self): return "Started"
    @abstractmethod
    def fuel_type(self): pass
class Car(Vehicle):
    def fuel_type(self): return "Petrol"
print("4.", Car().start(), Car().fuel_type())

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self): pass
class Developer(Employee):
    @property
    def salary(self): return 60000
print("5.", Developer().salary)

class Factory(ABC):
    @classmethod
    @abstractmethod
    def create(cls): pass
class UserFactory(Factory):
    @classmethod
    def create(cls): return {"type":"user"}
print("6.", UserFactory.create())

class Printable(ABC):
    @abstractmethod
    def print_data(self): pass
class Report(Printable):
    def print_data(self): return "Monthly Report"
print("7.", Report().print_data())

class Payment(ABC):
    @abstractmethod
    def pay(self,amount): pass
class Card(Payment):
    def pay(self,amount): return f"Card: {amount}"
class UPI(Payment):
    def pay(self,amount): return f"UPI: {amount}"
print("8.", [x.pay(1000) for x in [Card(),UPI()]])

class Repository(ABC):
    @abstractmethod
    def save(self,data): pass
class MemoryRepo(Repository):
    def __init__(self): self.data=[]
    def save(self,data): self.data.append(data)
r=MemoryRepo(); r.save("Python")
print("9.",r.data)

class Notification(ABC):
    @abstractmethod
    def send(self,msg): pass
class Email(Notification):
    def send(self,msg): return "Email: "+msg
class SMS(Notification):
    def send(self,msg): return "SMS: "+msg
print("10.",Email().send("Hello"),SMS().send("Hello"))

class Storage(ABC):
    @abstractmethod
    def put(self,k,v): pass
    @abstractmethod
    def get(self,k): pass
class DictStorage(Storage):
    def __init__(self): self.data={}
    def put(self,k,v): self.data[k]=v
    def get(self,k): return self.data.get(k)
st=DictStorage(); st.put("language","Python")
print("11.",st.get("language"))
