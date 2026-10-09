"""
Topic: Regular Expressions (Regex) for Data Cleaning
Description: Use the re module to find or replace text patterns.
Useful for cleaning text columns in datasets.
"""

import re


def clean_text(text):
    """Remove extra spaces and trim text."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_numbers(text):
    """Return all groups of digits found in text."""
    return re.findall(r"\d+", text)


if __name__ == "__main__":
    messy_text = "  Data    Analytics   with Python  "
    print("Clean text:", clean_text(messy_text))

    record = "Order 582 was placed on 2026-10-09"
    print("Numbers found:", extract_numbers(record))

    # Practice:
    # 1. Remove special characters from a string.
    # 2. Extract email-like patterns from sample text.
