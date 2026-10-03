"""99 - Email Validator"""
import re

EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

def is_valid_email(email):
    return bool(EMAIL_PATTERN.fullmatch(email.strip()))

def main():
    emails = [
        "riya@example.com",
        "invalid-email",
        "user.name@company.co.in",
        "test@",
    ]

    for email in emails:
        result = "Valid" if is_valid_email(email) else "Invalid"
        print(f"{email}: {result}")

if __name__ == "__main__":
    main()
