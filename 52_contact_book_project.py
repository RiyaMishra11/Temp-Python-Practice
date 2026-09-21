# Day 13 - 52: Contact Book Mini Project
# 10 practical operations

import json
from pathlib import Path

contacts = {}

# 1. Add contact
def add_contact(name, phone, email=""):
    contacts[name] = {"phone": phone, "email": email}

# 2. Show contacts
def show_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for name, info in sorted(contacts.items()):
        print(name, "-", info["phone"], "-", info["email"])

# 3. Search contact
def search_contact(keyword):
    keyword = keyword.lower()
    return {
        name: info for name, info in contacts.items()
        if keyword in name.lower() or keyword in info["phone"]
    }

# 4. Update phone
def update_phone(name, phone):
    if name not in contacts:
        return False
    contacts[name]["phone"] = phone
    return True

# 5. Update email
def update_email(name, email):
    if name not in contacts:
        return False
    contacts[name]["email"] = email
    return True

# 6. Delete contact
def delete_contact(name):
    return contacts.pop(name, None) is not None

# 7. Count contacts
def count_contacts():
    return len(contacts)

# 8. Find contacts without email
def missing_email():
    return [name for name, info in contacts.items() if not info["email"]]

# 9. Save contacts
def save_contacts(filename="contacts.json"):
    Path(filename).write_text(
        json.dumps(contacts, indent=2),
        encoding="utf-8"
    )

# 10. Load contacts
def load_contacts(filename="contacts.json"):
    path = Path(filename)
    if not path.exists():
        return False
    contacts.update(
        json.loads(path.read_text(encoding="utf-8"))
    )
    return True


add_contact("Aman", "9876543210", "aman@example.com")
add_contact("Riya", "9123456780", "riya@example.com")
add_contact("Rahul", "9988776655")

print("1. All contacts:")
show_contacts()

print("2. Search Riya:", search_contact("riya"))
print("3. Update phone:", update_phone("Rahul", "9000000000"))
print("4. Update email:", update_email("Rahul", "rahul@example.com"))
print("5. Count:", count_contacts())
print("6. Missing email:", missing_email())
print("7. Search 9000:", search_contact("9000"))
print("8. Delete Aman:", delete_contact("Aman"))

save_contacts()
print("9. Contacts saved to contacts.json")

contacts.clear()
print("10. Loaded:", load_contacts())
show_contacts()
