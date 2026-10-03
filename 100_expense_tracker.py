"""100 - Expense Tracker"""
import json
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path

@dataclass
class Expense:
    title: str
    amount: float
    category: str
    expense_date: str

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = Path(filename)
        self.expenses = self.load()

    def load(self):
        if not self.filename.exists():
            return []
        try:
            data = json.loads(self.filename.read_text(encoding="utf-8"))
            return [Expense(**item) for item in data]
        except (json.JSONDecodeError, OSError, TypeError):
            return []

    def save(self):
        self.filename.write_text(
            json.dumps([asdict(e) for e in self.expenses], indent=2),
            encoding="utf-8"
        )

    def add(self, title, amount, category):
        self.expenses.append(
            Expense(title, float(amount), category, date.today().isoformat())
        )
        self.save()

    def total(self):
        return sum(e.amount for e in self.expenses)

    def category_totals(self):
        totals = {}
        for expense in self.expenses:
            totals[expense.category] = totals.get(expense.category, 0) + expense.amount
        return totals

def main():
    tracker = ExpenseTracker()
    tracker.add("Lunch", 250, "Food")
    tracker.add("Bus", 80, "Travel")
    tracker.add("Groceries", 900, "Food")
    print("Total:", tracker.total())
    print("By category:", tracker.category_totals())

if __name__ == "__main__":
    main()
