# Day 6 - 21: SQLite Database Practice
import sqlite3

DB = "students.db"

# 1. Create a database table
def create_table():
    with sqlite3.connect(DB) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            marks REAL
        )""")

# 2. Insert one student
def insert_student(name, age, marks):
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO students(name, age, marks) VALUES(?, ?, ?)",
                     (name, age, marks))

# 3. Insert multiple students
def insert_many():
    data = [("Aman",20,85), ("Riya",21,92), ("Karan",19,76), ("Neha",22,88)]
    with sqlite3.connect(DB) as conn:
        conn.executemany("INSERT INTO students(name, age, marks) VALUES(?, ?, ?)", data)

# 4. Display all students
def show_all():
    with sqlite3.connect(DB) as conn:
        for row in conn.execute("SELECT * FROM students"):
            print(row)

# 5. Find students scoring above 80
def above_80():
    with sqlite3.connect(DB) as conn:
        for row in conn.execute("SELECT name, marks FROM students WHERE marks > 80"):
            print(row)

# 6. Find the highest scorer
def highest_scorer():
    with sqlite3.connect(DB) as conn:
        print(conn.execute("SELECT name, marks FROM students ORDER BY marks DESC LIMIT 1").fetchone())

# 7. Update marks
def update_marks(student_id, marks):
    with sqlite3.connect(DB) as conn:
        conn.execute("UPDATE students SET marks=? WHERE id=?", (marks, student_id))

# 8. Delete a student
def delete_student(student_id):
    with sqlite3.connect(DB) as conn:
        conn.execute("DELETE FROM students WHERE id=?", (student_id,))

# 9. Calculate average marks
def average_marks():
    with sqlite3.connect(DB) as conn:
        value = conn.execute("SELECT AVG(marks) FROM students").fetchone()[0]
        print("Average:", round(value or 0, 2))

# 10. Count students
def count_students():
    with sqlite3.connect(DB) as conn:
        print("Total students:", conn.execute("SELECT COUNT(*) FROM students").fetchone()[0])

if __name__ == "__main__":
    create_table()
    insert_many()
    show_all()
    above_80()
    highest_scorer()
    average_marks()
    count_students()
