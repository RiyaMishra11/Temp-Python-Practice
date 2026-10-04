"""102 - Contact Book"""
import json
from pathlib import Path

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = Path(filename)
        self.contacts = self.load()

    def load(self):
        if not self.filename.exists():
            return []
        try:
            return json.loads(self.filename.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []

    def save(self):
        self.filename.write_text(json.dumps(self.contacts, indent=2), encoding="utf-8")

    def add(self, name, phone, email):
        contact_id = max((c["id"] for c in self.contacts), default=0) + 1
        self.contacts.append({"id": contact_id, "name": name, "phone": phone, "email": email})
        self.save()
        return contact_id

    def search(self, keyword):
        keyword = keyword.lower()
        return [c for c in self.contacts if keyword in c["name"].lower()
                or keyword in c["phone"].lower() or keyword in c["email"].lower()]

    def delete(self, contact_id):
        old = len(self.contacts)
        self.contacts = [c for c in self.contacts if c["id"] != contact_id]
        if len(self.contacts) != old:
            self.save()
            return True
        return False

def main():
    book = ContactBook()
    book.add("Riya", "9876543210", "riya@example.com")
    book.add("Aman", "9123456780", "aman@example.com")
    print("Search results:", book.search("riya"))

if __name__ == "__main__":
    main()
