"""
Topic: Python Decorators
Description: A decorator adds behavior to a function without changing
the function's original code.
"""

def show_message(func):
    def wrapper():
        print("Function is starting...")
        func()
        print("Function has finished.")
    return wrapper


@show_message
def greet():
    print("Hello, Prashant!")


if __name__ == "__main__":
    greet()

    # Practice:
    # 1. Create a decorator that prints "Welcome".
    # 2. Decorate a function that displays a report title.
