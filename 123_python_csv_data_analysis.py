"""
Topic: CSV Data Analysis
Description: Read a CSV file, inspect rows, and calculate simple summaries
using Python's built-in csv module.
"""

import csv
from pathlib import Path


def analyze_csv(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"File not found: {path}")
        print("Create a CSV file named sales.csv with columns Product,Sales.")
        return

    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("The CSV file has no data rows.")
        return

    print("Number of records:", len(rows))
    print("Column names:", list(rows[0].keys()))

    if "Sales" in rows[0]:
        sales_values = []
        for row in rows:
            try:
                sales_values.append(float(row["Sales"]))
            except (TypeError, ValueError):
                continue

        if sales_values:
            print("Total sales:", sum(sales_values))
            print("Average sales:", sum(sales_values) / len(sales_values))
        else:
            print("No valid numeric values found in the Sales column.")


if __name__ == "__main__":
    # Put sales.csv in the same folder as this Python file.
    analyze_csv("sales.csv")

    # Example sales.csv:
    # Product,Sales
    # Laptop,45000
    # Mouse,800
    # Keyboard,1500

    # Practice:
    # 1. Add a Category column and count records by category.
    # 2. Find the product with the highest sales.
