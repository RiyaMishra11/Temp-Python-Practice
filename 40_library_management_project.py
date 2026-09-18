# Day 10 - 40: Library Management Mini Project
from dataclasses import dataclass, asdict
from pathlib import Path
import json

@dataclass
class Book:
    book_id: int
    title: str
    author: str
    available: bool = True

class Library:
    def __init__(self):
        self.books = {}

    # 1. Add book
    def add_book(self, book):
        self.books[book.book_id] = book

    # 2. Display books
    def show_books(self):
        for b in self.books.values():
            status = "Available" if b.available else "Issued"
            print(b.book_id, b.title, "-", b.author, "-", status)

    # 3. Search title
    def search_title(self, keyword):
        return [b for b in self.books.values() if keyword.lower() in b.title.lower()]

    # 4. Search author
    def search_author(self, keyword):
        return [b for b in self.books.values() if keyword.lower() in b.author.lower()]

    # 5. Issue book
    def issue_book(self, book_id):
        b = self.books.get(book_id)
        if not b: return "Book not found"
        if not b.available: return "Already issued"
        b.available = False
        return "Issued successfully"

    # 6. Return book
    def return_book(self, book_id):
        b = self.books.get(book_id)
        if not b: return "Book not found"
        b.available = True
        return "Returned successfully"

    # 7. Delete book
    def delete_book(self, book_id):
        return self.books.pop(book_id, None) is not None

    # 8. Count available books
    def available_count(self):
        return sum(b.available for b in self.books.values())

    # 9. Save to JSON
    def save(self, filename="library.json"):
        data = [asdict(b) for b in self.books.values()]
        Path(filename).write_text(json.dumps(data, indent=2), encoding="utf-8")

    # 10. Load from JSON
    def load(self, filename="library.json"):
        path = Path(filename)
        if not path.exists(): return False
        data = json.loads(path.read_text(encoding="utf-8"))
        self.books = {x["book_id"]: Book(**x) for x in data}
        return True

# Demo
library = Library()
library.add_book(Book(1, "Python Basics", "John Smith"))
library.add_book(Book(2, "Clean Code", "Robert Martin"))
library.add_book(Book(3, "Data Structures", "Mark Allen"))

print("Books:")
library.show_books()
print("Search:", library.search_title("python"))
print("Issue:", library.issue_book(1))
print("Return:", library.return_book(1))
print("Available:", library.available_count())
print("Delete book 3:", library.delete_book(3))
library.save()
print("Saved to library.json")

new_library = Library()
print("Loaded:", new_library.load())
new_library.show_books()
