# Day 11 - 44: Student Management Mini Project
import json
from pathlib import Path

students = {}

# 1. Add student
def add_student(roll, name, marks):
    students[roll] = {"name": name, "marks": marks}

# 2. Total marks
def total(roll):
    return sum(students[roll]["marks"])

# 3. Average
def average(roll):
    return total(roll) / len(students[roll]["marks"])

# 4. Grade
def grade(roll):
    a = average(roll)
    if a >= 90: return "A+"
    if a >= 80: return "A"
    if a >= 70: return "B"
    if a >= 60: return "C"
    if a >= 50: return "D"
    return "F"

# 5. Topper
def topper():
    return max(students, key=average)

# 6. Passed students
def passed():
    return [s["name"] for s in students.values() if min(s["marks"]) >= 40]

# 7. Search
def search(name):
    return [s for s in students.values() if name.lower() in s["name"].lower()]

# 8. Delete
def delete(roll):
    return students.pop(roll, None) is not None

# 9. Save JSON
def save(filename="students.json"):
    Path(filename).write_text(json.dumps(students, indent=2), encoding="utf-8")

# 10. Load JSON
def load(filename="students.json"):
    p = Path(filename)
    if not p.exists(): return False
    students.update(json.loads(p.read_text(encoding="utf-8")))
    return True

add_student(101, "Aman", [85,90,78])
add_student(102, "Riya", [95,92,96])
add_student(103, "Rahul", [65,72,68])

print("1. Students:", students)
print("2. Aman total:", total(101))
print("3. Aman average:", round(average(101), 2))
print("4. Riya grade:", grade(102))
print("5. Topper:", students[topper()]["name"])
print("6. Passed:", passed())
print("7. Search Riya:", search("riya"))
print("8. Delete Rahul:", delete(103))
save()
print("9. Saved to students.json")
students.clear()
print("10. Loaded:", load())
print(students)
