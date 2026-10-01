"""91 - Secure Password Generator"""
import secrets
import string

def generate_password(length=16, uppercase=True, digits=True, symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    alphabet = string.ascii_lowercase
    if uppercase:
        alphabet += string.ascii_uppercase
    if digits:
        alphabet += string.digits
    if symbols:
        alphabet += "!@#$%^&*()-_=+"

    return "".join(secrets.choice(alphabet) for _ in range(length))

def main():
    try:
        length = int(input("Password length (default 16): ") or "16")
        print("Generated password:", generate_password(length))
    except ValueError as exc:
        print("Error:", exc)

if __name__ == "__main__":
    main()
