# 115 Custom Iterators and Iterables

# 1 List iterator
print("1.", list(iter([1, 2, 3])))

# 2 Manual next()
iterator = iter([10, 20, 30])
print("2.", next(iterator), next(iterator))

# 3 Custom countdown iterator
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("3.", list(Countdown(5)))

# 4 Range-like iterable
class NumberRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        current = self.start
        while current < self.stop:
            yield current
            current += 1

print("4.", list(NumberRange(2, 7)))

# 5 Generator expression
print("5.", list(x * x for x in range(5)))

# 6 Generator function
def even_numbers(limit):
    for number in range(limit + 1):
        if number % 2 == 0:
            yield number

print("6.", list(even_numbers(10)))

# 7 Counter generator
def counter(start=0):
    while True:
        yield start
        start += 1

counter_obj = counter(10)
print("7.", [next(counter_obj) for _ in range(5)])

# 8 yield from
def combined():
    yield from [1, 2, 3]
    yield from [4, 5]

print("8.", list(combined()))

# 9 Custom iterable
class Team:
    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)

print("9.", list(Team(["Aman", "Riya", "Rahul"])))

# 10 Indexed iterable
class Indexed:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        yield from enumerate(self.items)

print("10.", list(Indexed(["Python", "Java", "Go"])))

# 11 Chunk generator
def chunks(items, size):
    for index in range(0, len(items), size):
        yield items[index:index + size]

print("11.", list(chunks(list(range(1, 11)), 3)))
