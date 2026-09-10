# Strings, Lists, Tuples and Dictionaries

# 1. Find the length of a string
text = input("Enter a string: ")
print("Length:", len(text))

# 2. Reverse a string
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

# 3. Check whether a string is a palindrome
text = input("Enter a string: ")
cleaned = text.lower().replace(" ", "")
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 4. Count vowels in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)

# 5. Count words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

# 6. Find the largest element in a list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Largest element:", max(numbers))

# 7. Find the sum of all elements in a list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sum:", sum(numbers))

# 8. Remove duplicate elements from a list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = list(dict.fromkeys(numbers))
print("List without duplicates:", unique_numbers)

# 9. Create a dictionary of student details
name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter course: ")
student = {"name": name, "age": age, "course": course}
print("Student details:", student)

# 10. Count frequency of each character
text = input("Enter a string: ")
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print("Character frequency:", frequency)
