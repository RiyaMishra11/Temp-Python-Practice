# Python Practice - JSON and CSV
import json, csv

# 1. Dictionary to JSON
student={"name":"Riya","marks":92}; print(json.dumps(student,indent=2))

# 2. JSON to dictionary
data=json.loads('{"name":"Aman","marks":85}'); print(data)

# 3. Write JSON file
profile={"name":"User","language":"Python"}
with open("profile.json","w") as f: json.dump(profile,f,indent=2)
print("profile.json created")

# 4. Read JSON file
with open("profile.json") as f: print(json.load(f))

# 5. Student records
students=[{"name":"Aman","marks":78},{"name":"Riya","marks":92},{"name":"Karan","marks":85}]
print(students)

# 6. Create CSV file
rows=[["Name","Marks"],["Aman",78],["Riya",92],["Karan",85]]
with open("students.csv","w",newline="") as f: csv.writer(f).writerows(rows)
print("students.csv created")

# 7. Read CSV file
with open("students.csv") as f:
    for row in csv.reader(f): print(row)

# 8. Average marks
marks=[78,92,85,88]; print("Average:",sum(marks)/len(marks))

# 9. Highest scorer
top=max(students,key=lambda x:x["marks"]); print("Top:",top)

# 10. Convert CSV rows to dictionaries
with open("students.csv") as f: print(list(csv.DictReader(f)))
