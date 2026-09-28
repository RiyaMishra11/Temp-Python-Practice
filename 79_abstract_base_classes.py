# Python Practice 79: Abstract Base Classes & Polymorphism
from abc import ABC, abstractmethod

# 1. Basic abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self): pass

class Dog(Animal):
    def sound(self): return "Bark"

print("1.", Dog().sound())

# 2. Multiple abstract methods
class Vehicle(ABC):
    @abstractmethod
    def start(self): pass
    @abstractmethod
    def stop(self): pass

class Car(Vehicle):
    def start(self): return "Car started"
    def stop(self): return "Car stopped"

car = Car()
print("2.", car.start(), "|", car.stop())

# 3. Concrete method inside abstract class
class Employee(ABC):
    @abstractmethod
    def role(self): pass
    def company_policy(self): return "Follow company policy"

class Developer(Employee):
    def role(self): return "Developer"

print("3.", Developer().role(), "|", Developer().company_policy())

# 4. Abstract property
class Shape(ABC):
    @property
    @abstractmethod
    def area(self): pass

class Square(Shape):
    def __init__(self, side): self.side = side
    @property
    def area(self): return self.side ** 2

print("4. Area:", Square(5).area)

# 5. Abstract classmethod
class Parser(ABC):
    @classmethod
    @abstractmethod
    def from_text(cls, text): pass

class NumberParser(Parser):
    @classmethod
    def from_text(cls, text): return cls(), int(text)

print("5.", NumberParser.from_text("42")[1])

# 6. Abstract staticmethod
class Validator(ABC):
    @staticmethod
    @abstractmethod
    def validate(value): pass

class PositiveValidator(Validator):
    @staticmethod
    def validate(value): return value > 0

print("6.", PositiveValidator.validate(10))

# 7. Polymorphism
class Payment(ABC):
    @abstractmethod
    def pay(self, amount): pass

class CardPayment(Payment):
    def pay(self, amount): return f"Card: ₹{amount}"

class UpiPayment(Payment):
    def pay(self, amount): return f"UPI: ₹{amount}"

print("7.", [p.pay(500) for p in [CardPayment(), UpiPayment()]])

# 8. Virtual subclass
class Printable(ABC):
    @abstractmethod
    def print_data(self): pass

class Report:
    def print_data(self): return "Report printed"

Printable.register(Report)
print("8.", isinstance(Report(), Printable))

# 9. Repository pattern
class Repository(ABC):
    @abstractmethod
    def save(self, item): pass
    @abstractmethod
    def all(self): pass

class MemoryRepository(Repository):
    def __init__(self): self.items = []
    def save(self, item): self.items.append(item)
    def all(self): return self.items.copy()

repo = MemoryRepository()
repo.save("Python")
repo.save("GitHub")
print("9.", repo.all())

# 10. Template-style service
class NotificationService(ABC):
    def send(self, message):
        self.validate(message)
        return self._send(message)
    def validate(self, message):
        if not message.strip(): raise ValueError("Empty message")
    @abstractmethod
    def _send(self, message): pass

class EmailService(NotificationService):
    def _send(self, message): return f"Email sent: {message}"

print("10.", EmailService().send("Hello"))

# 11. Abstract database
class Database(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def query(self, sql): pass

class SQLiteDatabase(Database):
    def connect(self): return "SQLite connected"
    def query(self, sql): return f"Executing: {sql}"

db = SQLiteDatabase()
print("11.", db.connect(), "|", db.query("SELECT * FROM users"))
