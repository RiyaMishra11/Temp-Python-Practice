# Day 6 - 24: CLI and Project Structure Practice
import argparse
import os
import sys
from pathlib import Path

# 1. Read command-line arguments
def show_arguments():
    print("Script:", sys.argv[0])
    print("Arguments:", sys.argv[1:])

# 2. Parse a greeting argument
def greeting(name="User"):
    print(f"Hello, {name}!")

# 3. CLI-style calculator function
def calculator(a, b, operation="add"):
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Cannot divide by zero"
    }
    return operations.get(operation, "Invalid operation")

# 4. Read environment variable
def environment_demo():
    print("USER_NAME:", os.getenv("USER_NAME", "Guest"))

# 5. Create project folders
def create_structure():
    folders = ["my_project/src", "my_project/tests", "my_project/data", "my_project/docs"]
    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
    print("Folders created.")

# 6. Create starter files
def create_files():
    names = ["my_project/src/main.py", "my_project/src/utils.py",
             "my_project/tests/test_main.py", "my_project/README.md"]
    for name in names:
        path = Path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)
    print("Starter files created.")

# 7. List Python files
def list_python_files(directory="."):
    for path in sorted(Path(directory).glob("*.py")):
        print(path.name)

# 8. Count file lines
def count_lines(filename):
    path = Path(filename)
    if path.exists():
        print(filename, "has", len(path.read_text(encoding="utf-8").splitlines()), "lines.")
    else:
        print("File not found.")

# 9. Command dispatcher
def dispatch(command):
    commands = {
        "hello": lambda: print("Hello!"),
        "status": lambda: print("Project is active."),
        "version": lambda: print("Version 1.0.0")
    }
    commands.get(command, lambda: print("Unknown command"))()

# 10. Simple menu
def menu():
    options = {"1": "Add task", "2": "View tasks", "3": "Delete task", "4": "Exit"}
    for key, value in options.items():
        print(f"{key}. {value}")
    choice = input("Choose: ").strip()
    print("Selected:", options.get(choice, "Invalid option"))

if __name__ == "__main__":
    greeting("Python Developer")
    environment_demo()
    print("Calculator:", calculator(20, 5, "multiply"))
    create_structure()
    create_files()
    dispatch("status")
