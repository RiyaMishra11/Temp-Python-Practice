"""103 - Password Strength Checker"""
import re

def check_password_strength(password):
    score = 0
    suggestions = []

    checks = [
        (len(password) >= 8, "Use at least 8 characters."),
        (bool(re.search(r"[A-Z]", password)), "Add an uppercase letter."),
        (bool(re.search(r"[a-z]", password)), "Add a lowercase letter."),
        (bool(re.search(r"\d", password)), "Add a number."),
        (bool(re.search(r"[^A-Za-z0-9]", password)), "Add a special character.")
    ]

    for passed, suggestion in checks:
        if passed:
            score += 1
        else:
            suggestions.append(suggestion)

    levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return levels[score], suggestions

def main():
    password = input("Enter password to check: ")
    strength, suggestions = check_password_strength(password)
    print("Strength:", strength)
    for suggestion in suggestions:
        print("-", suggestion)

if __name__ == "__main__":
    main()
