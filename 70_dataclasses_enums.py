"""Day 17 - File 70: Dataclasses and Enums | 11 Programs"""
from dataclasses import dataclass, field
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    ACTIVE = auto()
    COMPLETED = auto()

@dataclass
class Student:
    name: str
    age: int
    marks: float

def program_1():
    print(Student("Aman", 21, 88.5))

def program_2():
    student = Student("Riya", 22, 91)
    print(student.name, student.marks)

def program_3():
    print(Student("Aman", 21, 88) == Student("Aman", 21, 88))

def program_4():
    students = [Student("Aman",21,82), Student("Riya",22,95), Student("Kabir",20,89)]
    print(sorted(students, key=lambda x: x.marks, reverse=True))

@dataclass
class Employee:
    name: str
    salary: int
    department: str = "IT"

def program_5():
    print(Employee("Neha", 55000))

@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)

def program_6():
    team = Team("Python Team")
    team.members.extend(["Aman", "Riya", "Kabir"])
    print(team)

def program_7():
    for status in Status:
        print(status.name, status.value)

def program_8():
    current = Status.ACTIVE
    print(current == Status.ACTIVE)
    print(current == Status.COMPLETED)

def program_9():
    print(Status["COMPLETED"])

def program_10():
    employees = [
        Employee("Aman",50000,"IT"),
        Employee("Riya",65000,"HR"),
        Employee("Kabir",72000,"IT")
    ]
    print("Count:", len(employees))
    print("Total salary:", sum(e.salary for e in employees))
    print("Highest:", max(employees, key=lambda e:e.salary))

@dataclass
class Task:
    title: str
    status: Status = Status.PENDING

def program_11():
    tasks = [
        Task("Learn Python"),
        Task("Build project", Status.ACTIVE),
        Task("Push to GitHub", Status.COMPLETED)
    ]
    for task in tasks:
        print(task.title, "->", task.status.name)

if __name__ == "__main__":
    program_1()
