"""File 76: Properties and Descriptors | 11 Programs"""

def program_1():
    class Person:
        def __init__(self,name):self._name=name
        @property
        def name(self):return self._name
    print(Person("Aman").name)

def program_2():
    class Account:
        def __init__(self,balance):self.balance=balance
        @property
        def balance(self):return self._balance
        @balance.setter
        def balance(self,v):
            if v<0:raise ValueError("Negative balance")
            self._balance=v
    a=Account(5000);a.balance=7500;print(a.balance)

def program_3():
    class Rectangle:
        def __init__(self,l,w):self.l=l;self.w=w
        @property
        def area(self):return self.l*self.w
    print(Rectangle(10,5).area)

def program_4():
    class Student:
        def __init__(self,m):self.marks=m
        @property
        def marks(self):return self._marks
        @marks.setter
        def marks(self,v):
            if not 0<=v<=100:raise ValueError("0-100 only")
            self._marks=v
    print(Student(88).marks)

def program_5():
    class Circle:
        def __init__(self,r):self.r=r
        @property
        def diameter(self):return self.r*2
    print(Circle(7).diameter)

def program_6():
    class Positive:
        def __set_name__(self,owner,name):self.name=name
        def __get__(self,obj,owner):
            return self if obj is None else obj.__dict__.get(self.name)
        def __set__(self,obj,v):
            if v<=0:raise ValueError("Must be positive")
            obj.__dict__[self.name]=v
    class Product:price=Positive()
    print(Product().price if False else end_demo(Product))

def end_demo(cls):
    p=cls();p.price=1200;return p.price

def program_7():
    class NonEmpty:
        def __set_name__(self,owner,name):self.name=name
        def __get__(self,obj,owner):return self if obj is None else obj.__dict__.get(self.name,"")
        def __set__(self,obj,v):
            if not isinstance(v,str) or not v.strip():raise ValueError("Non-empty string required")
            obj.__dict__[self.name]=v
    class User:name=NonEmpty()
    print(User().name if False else user_demo(User))

def user_demo(cls):
    u=cls();u.name="Riya";return u.name

def program_8():
    class Config:
        host="localhost"
        def __getattr__(self,name):return "Unknown setting: "+name
    c=Config();print(c.host,c.port)

def program_9():
    class Temperature:
        def __setattr__(self,name,v):
            if name=="celsius" and v<-273.15:raise ValueError("Below absolute zero")
            super().__setattr__(name,v)
    t=Temperature();t.celsius=25;print(t.celsius)

def program_10():
    class SafeUser:
        allowed={"name","age"}
        def __setattr__(self,n,v):
            if n not in self.allowed:raise AttributeError(n+" not allowed")
            object.__setattr__(self,n,v)
    u=SafeUser();u.name="Kabir";u.age=21;print(u.name,u.age)

def program_11():
    class PositiveInt:
        def __set_name__(self,o,n):self.name=n
        def __get__(self,obj,o):return self if obj is None else obj.__dict__.get(self.name)
        def __set__(self,obj,v):
            if not isinstance(v,int) or v<=0:raise ValueError(self.name+" must be positive")
            obj.__dict__[self.name]=v
    class Order:
        quantity=PositiveInt();price=PositiveInt()
        def __init__(self,q,p):self.quantity=q;self.price=p
        @property
        def total(self):return self.quantity*self.price
    o=Order(3,1200);print(o.quantity,o.price,o.total)

if __name__=="__main__":program_1()
