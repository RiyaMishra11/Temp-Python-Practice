"""SQLite database basics using Python's built-in sqlite3 module."""
import sqlite3
from pathlib import Path

DB_FILE = Path("company.db")

def main():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL
            )
        """)
        cursor.execute(
            "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
            ("Prashant", "Analytics", 32000)
        )
        cursor.execute("SELECT employee_id, name, department, salary FROM employees")
        for row in cursor.fetchall():
            print(row)
        connection.commit()

if __name__ == "__main__":
    main()
    # Practice: query employees earning more than 30000.
    # Note: each run adds another sample row.
