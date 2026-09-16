# Day 7 - 25: Searching Algorithms

def linear_search(items, target):  # 1. Linear search
    for i, value in enumerate(items):
        if value == target: return i
    return -1

def find_all(items, target):  # 2. Find all occurrences
    return [i for i, value in enumerate(items) if value == target]

def search_word(text, word):  # 3. Search word in text
    return word.lower() in text.lower()

def find_max(numbers):  # 4. Maximum without max()
    result = numbers[0]
    for n in numbers[1:]:
        if n > result: result = n
    return result

def find_min(numbers):  # 5. Minimum without min()
    result = numbers[0]
    for n in numbers[1:]:
        if n < result: result = n
    return result

def second_largest(numbers):  # 6. Second largest
    values = sorted(set(numbers), reverse=True)
    return values[1] if len(values) > 1 else None

def binary_search(items, target):  # 7. Binary search
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target: return mid
        if items[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1

def count_greater(numbers, target):  # 8. Count values greater than target
    return sum(n > target for n in numbers)

def first_even(numbers):  # 9. Find first even number
    return next((n for n in numbers if n % 2 == 0), None)

def longest_word(words):  # 10. Find longest word
    return max(words, key=len) if words else None

if __name__ == "__main__":
    data = [10, 25, 7, 25, 42, 18]
    print(linear_search(data, 42), find_all(data, 25))
    print(search_word("Python programming", "PYTHON"))
    print(find_max(data), find_min(data), second_largest(data))
    print(binary_search(sorted(data), 25))
    print(count_greater(data, 20), first_even(data))
    print(longest_word(["Python", "Java", "Programming"]))
