# Python Practice - Dictionaries and Sets

# 1. Student dictionary
student = {"name": input("Name: "), "age": int(input("Age: ")), "course": input("Course: ")}
print(student)

# 2. Safe dictionary lookup
student = {"name": "Rahul", "age": 20, "course": "Python"}
key = input("Enter key: ")
print(student.get(key, "Key not found"))

# 3. Add and update dictionary values
person = {"name": "Amit", "age": 21}
person["city"] = input("City: ")
person["age"] = int(input("Updated age: "))
print(person)

# 4. Student with highest marks
students = {"Aman": 78, "Riya": 92, "Karan": 85, "Neha": 88}
top = max(students, key=students.get)
print("Top student:", top, "Marks:", students[top])

# 5. Word frequency
sentence = input("Enter sentence: ").lower()
freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)

# 6. Unique elements using set
numbers = list(map(int, input("Enter numbers: ").split()))
print("Unique:", set(numbers))

# 7. Set union, intersection and difference
a = set(input("First set: ").split())
b = set(input("Second set: ").split())
print("Union:", a | b)
print("Intersection:", a & b)
print("A-B:", a - b)
print("B-A:", b - a)

# 8. Check disjoint sets
a = set(input("First set: ").split())
b = set(input("Second set: ").split())
print("Disjoint" if a.isdisjoint(b) else "Not disjoint")

# 9. Create dictionary from two lists
keys = input("Keys: ").split()
values = input("Values: ").split()
print(dict(zip(keys, values)) if len(keys) == len(values) else "Lengths must match")

# 10. Group numbers as even and odd
numbers = list(map(int, input("Enter numbers: ").split()))
grouped = {"even": [n for n in numbers if n % 2 == 0],
           "odd": [n for n in numbers if n % 2 != 0]}
print(grouped)
