"""
Topic: Python Generators
Description: Learn how to generate values one at a time using yield.
"""

def number_generator(limit):
    """Generate numbers from 1 to limit one at a time."""
    number = 1
    while number <= limit:
        yield number
        number += 1


if __name__ == "__main__":
    for value in number_generator(5):
        print(value)

    # Practice:
    # 1. Create a generator for even numbers.
    # 2. Generate squares from 1 to 10.
