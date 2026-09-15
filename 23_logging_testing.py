# Day 6 - 23: Logging and Testing Practice
import logging
import unittest

# 1. Configure logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.info("Logging started.")

# 2. Log different levels
def log_messages():
    logging.debug("Debug message")
    logging.info("Info message")
    logging.warning("Warning message")
    logging.error("Error message")

# 3. Log a calculation
def calculate_total(price, quantity):
    total = price * quantity
    logging.info("Total calculated: %s", total)
    return total

# 4. Validate with assertion
def validate_age(age):
    assert age >= 18, "Age must be 18 or above"
    return True

# 5. Check even numbers
def is_even(number):
    return number % 2 == 0

def test_even():
    assert is_even(10)
    assert not is_even(7)
    print("Even-number assertions passed.")

# 6. Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 7. Test calculator
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

# 8. String function
def make_upper(text):
    return text.upper()

# 9. Test string function
class TestString(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(make_upper("python"), "PYTHON")

# 10. Test password validation
def strong_password(password):
    return (len(password) >= 8
            and any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password))

class TestPassword(unittest.TestCase):
    def test_strong(self):
        self.assertTrue(strong_password("Python123"))

    def test_weak(self):
        self.assertFalse(strong_password("python"))

if __name__ == "__main__":
    setup_logging()
    calculate_total(250, 3)
    test_even()
    unittest.main(verbosity=2)
