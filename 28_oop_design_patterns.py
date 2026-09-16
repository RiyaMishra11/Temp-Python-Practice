# Day 7 - 28: OOP and Simple Design Patterns

class Person:  # 1. Basic class
    def __init__(self,name,age): self.name,self.age=name,age
    def introduce(self): return f"{self.name} is {self.age} years old."

class BankAccount:  # 2. Bank account
    def __init__(self,owner,balance=0): self.owner,self.balance=owner,balance
    def deposit(self,amount): self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance: self.balance-=amount; return True
        return False

class Employee(Person):  # 3. Inheritance
    def __init__(self,name,age,salary):
        super().__init__(name,age); self.salary=salary
    def work(self): return f"{self.name} is working."

class Manager(Employee):  # 4. Method overriding
    def work(self): return f"{self.name} is managing the team."

class Temperature:  # 5. Property / encapsulation
    def __init__(self,celsius=0): self._celsius=celsius
    @property
    def celsius(self): return self._celsius
    @celsius.setter
    def celsius(self,value):
        if value < -273.15: raise ValueError("Below absolute zero")
        self._celsius=value

class Product:  # 6. Class method
    def __init__(self,name,price): self.name,self.price=name,price
    @classmethod
    def from_string(cls,text):
        name,price=text.split(","); return cls(name.strip(),float(price))

class MathHelper:  # 7. Static method
    @staticmethod
    def square(n): return n*n

class Engine:
    def start(self): return "Engine started."

class Car:  # 8. Composition
    def __init__(self): self.engine=Engine()
    def start(self): return self.engine.start()

class AppConfig:  # 9. Shared configuration
    settings={}
    @classmethod
    def set(cls,key,value): cls.settings[key]=value
    @classmethod
    def get(cls,key,default=None): return cls.settings.get(key,default)

class Dog:  # 10. Polymorphism
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

def make_speak(animals):
    for animal in animals: print(animal.speak())

if __name__ == "__main__":
    print(Person("Aman",21).introduce())
    account=BankAccount("Riya",1000); account.deposit(500); account.withdraw(250)
    print("Balance:",account.balance)
    print(Manager("Karan",30,60000).work())
    t=Temperature(25); t.celsius=30; print(t.celsius)
    p=Product.from_string("Laptop,55000"); print(p.name,p.price)
    print(MathHelper.square(8))
    print(Car().start())
    AppConfig.set("mode","development"); print(AppConfig.get("mode"))
    make_speak([Dog(),Cat()])
