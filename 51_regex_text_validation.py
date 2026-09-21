# Day 13 - 51: Regular Expressions and Text Validation
# 10 practical programs

import re

# 1. Validate email
def valid_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return bool(re.fullmatch(pattern, email))

# 2. Validate phone number
def valid_phone(phone):
    return bool(re.fullmatch(r"\d{10}", phone))

# 3. Find all numbers
def extract_numbers(text):
    return re.findall(r"\d+", text)

# 4. Find all words
def extract_words(text):
    return re.findall(r"[A-Za-z]+", text)

# 5. Replace multiple spaces
def normalize_spaces(text):
    return re.sub(r"\s+", " ", text).strip()

# 6. Mask an email
def mask_email(email):
    user, domain = email.split("@", 1)
    if len(user) <= 2:
        masked = "*" * len(user)
    else:
        masked = user[0] + "*" * (len(user)-2) + user[-1]
    return masked + "@" + domain

# 7. Validate password strength
def strong_password(password):
    return (
        len(password) >= 8
        and bool(re.search(r"[A-Z]", password))
        and bool(re.search(r"[a-z]", password))
        and bool(re.search(r"\d", password))
        and bool(re.search(r"[^A-Za-z0-9]", password))
    )

# 8. Find hashtags
def hashtags(text):
    return re.findall(r"#[A-Za-z0-9_]+", text)

# 9. Extract dates
def dates(text):
    return re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)

# 10. Count occurrences of a word
def word_count(text, word):
    return len(re.findall(r"\b" + re.escape(word) + r"\b", text, re.I))


print("1. Email:", valid_email("student@example.com"))
print("2. Phone:", valid_phone("9876543210"))
print("3. Numbers:", extract_numbers("I have 25 books and 3 pens."))
print("4. Words:", extract_words("Python 3 is powerful!"))
print("5. Spaces:", normalize_spaces("Python    is   easy."))
print("6. Masked email:", mask_email("student@example.com"))
print("7. Strong password:", strong_password("Python@123"))
print("8. Hashtags:", hashtags("Learning #Python and #Coding"))
print("9. Dates:", dates("Exam: 21-09-2026, Result: 30-09-2026"))
print("10. Word count:", word_count("Python is easy. Python is powerful.", "Python"))
