"""90 - CSV Data Analyzer"""
import csv
from pathlib import Path
from statistics import mean

class CSVDataAnalyzer:
    def __init__(self, filename: str):
        self.filename = Path(filename)
        self.rows = []

    def load(self):
        with self.filename.open("r", encoding="utf-8", newline="") as file:
            self.rows = list(csv.DictReader(file))
        return self.rows

    def numeric_stats(self, column: str):
        values = []
        for row in self.rows:
            try:
                values.append(float(row[column]))
            except (KeyError, ValueError):
                pass
        if not values:
            raise ValueError(f"No numeric values found for {column}")
        return {
            "count": len(values),
            "average": mean(values),
            "minimum": min(values),
            "maximum": max(values),
        }

    def filter_rows(self, column: str, value: str):
        return [row for row in self.rows if row.get(column) == value]

def main():
    filename = "students.csv"
    rows = [
        {"name": "Riya", "score": "92", "department": "Python"},
        {"name": "Aman", "score": "85", "department": "Backend"},
        {"name": "Neha", "score": "96", "department": "Python"},
    ]
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    analyzer = CSVDataAnalyzer(filename)
    analyzer.load()
    print("Score statistics:", analyzer.numeric_stats("score"))
    print("Python department:", analyzer.filter_rows("department", "Python"))

if __name__ == "__main__":
    main()
