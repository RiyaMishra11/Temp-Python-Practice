"""107 - Student Grade Manager"""

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(float(grade))

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def status(self):
        return "Pass" if self.average() >= 40 else "Needs Improvement"

class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = Student(name)

    def add_grade(self, name, grade):
        self.students[name].add_grade(grade)

    def report(self):
        return [
            {"name": s.name, "average": round(s.average(), 2), "status": s.status()}
            for s in self.students.values()
        ]

def main():
    book = GradeBook()
    book.add_student("Riya")
    book.add_student("Aman")

    for grade in (85, 92, 78):
        book.add_grade("Riya", grade)
    for grade in (55, 61, 48):
        book.add_grade("Aman", grade)

    for student in book.report():
        print(student)

if __name__ == "__main__":
    main()
