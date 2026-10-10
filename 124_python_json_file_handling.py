"""JSON file handling: save and load structured data."""
import json
from pathlib import Path

DATA_FILE = Path("employees.json")

def save_employees(employees, file_path=DATA_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(employees, file, indent=4)
    print(f"Data saved to {file_path}")

def load_employees(file_path=DATA_FILE):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

if __name__ == "__main__":
    employees = [
        {"name": "Prashant", "department": "Analytics", "salary": 32000},
        {"name": "Riya", "department": "IT", "salary": 35000},
    ]
    save_employees(employees)
    for employee in load_employees():
        print(employee)

    # Practice: calculate the average salary from the loaded data.
