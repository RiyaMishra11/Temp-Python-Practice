# Day 12 - 47: File Handling, CSV and JSON
import csv
import json
from pathlib import Path

# 1. Write a text file
Path("notes.txt").write_text("Python file handling\nLearning CSV and JSON", encoding="utf-8")
print("1. Text file written")

# 2. Read a text file
print("2.", Path("notes.txt").read_text(encoding="utf-8"))

# 3. Count lines
content = Path("notes.txt").read_text(encoding="utf-8")
print("3. Lines:", len(content.splitlines()))

# 4. Count words
print("4. Words:", len(content.split()))

# 5. Write CSV
rows = [
    ["Name", "Age", "Course"],
    ["Riya", 21, "Python"],
    ["Aman", 22, "Data Science"]
]
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)
print("5. CSV written")

# 6. Read CSV
with open("students.csv", newline="", encoding="utf-8") as f:
    csv_data = list(csv.reader(f))
print("6.", csv_data)

# 7. Write JSON
data = {"name": "Riya", "skills": ["Python", "GitHub"], "active": True}
Path("profile.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
print("7. JSON written")

# 8. Read JSON
loaded = json.loads(Path("profile.json").read_text(encoding="utf-8"))
print("8.", loaded)

# 9. Search files in current directory
py_files = [p.name for p in Path(".").glob("*.py")]
print("9. Python files:", py_files)

# 10. Create a simple backup copy
Path("notes_backup.txt").write_text(content, encoding="utf-8")
print("10. Backup created")
