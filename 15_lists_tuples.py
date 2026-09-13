# Python Practice - Lists and Tuples

# 1. Create and display a list
numbers = list(map(int, input("Enter numbers: ").split()))
print("List:", numbers)

# 2. Second largest element
numbers = list(map(int, input("Enter numbers: ").split()))
unique = sorted(set(numbers))
print("Second largest:", unique[-2] if len(unique) >= 2 else "Not available")

# 3. Count positive, negative and zero
numbers = list(map(int, input("Enter numbers: ").split()))
print("Positive:", sum(n > 0 for n in numbers))
print("Negative:", sum(n < 0 for n in numbers))
print("Zero:", numbers.count(0))

# 4. Separate even and odd
numbers = list(map(int, input("Enter numbers: ").split()))
print("Even:", [n for n in numbers if n % 2 == 0])
print("Odd:", [n for n in numbers if n % 2 != 0])

# 5. Sort ascending and descending
numbers = list(map(int, input("Enter numbers: ").split()))
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))

# 6. Search an element
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))
print("Found at index:", numbers.index(target) if target in numbers else "Not found")

# 7. List slicing
items = input("Enter items: ").split()
print("First 3:", items[:3])
print("Last 3:", items[-3:])
print("Reverse:", items[::-1])

# 8. Remove duplicates preserving order
numbers = list(map(int, input("Enter numbers: ").split()))
result = []
for n in numbers:
    if n not in result: result.append(n)
print("Unique:", result)

# 9. Common elements of two lists
a = input("First list: ").split()
b = input("Second list: ").split()
print("Common:", list(dict.fromkeys(x for x in a if x in b)))

# 10. Tuple operations
values = tuple(input("Enter tuple values: ").split())
print("Tuple:", values)
print("Length:", len(values))
print("First:", values[0] if values else "Empty")
print("Last:", values[-1] if values else "Empty")
print("Reversed:", values[::-1])
