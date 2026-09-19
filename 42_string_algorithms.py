# Day 11 - 42: String Algorithms
from collections import Counter

# 1. Reverse
text = "Python"
print("1.", text[::-1])

# 2. Palindrome
text = "madam"
print("2. Palindrome:", text == text[::-1])

# 3. Vowels and consonants
text = "Programming"
vowels = "aeiou"
v = sum(c.lower() in vowels for c in text if c.isalpha())
c = sum(c.isalpha() and c.lower() not in vowels for c in text)
print("3. Vowels:", v, "Consonants:", c)

# 4. Remove duplicate characters
print("4.", "".join(dict.fromkeys("programming")))

# 5. Longest word
sentence = "Python makes programming interesting"
print("5.", max(sentence.split(), key=len))

# 6. Rotation check
a, b = "waterbottle", "erbottlewat"
print("6. Rotation:", len(a) == len(b) and b in a + a)

# 7. Character frequency
print("7.", dict(Counter("banana")))

# 8. First repeated character
text = "abcdefca"
seen, repeat = set(), None
for c in text:
    if c in seen:
        repeat = c
        break
    seen.add(c)
print("8.", repeat)

# 9. Run-length encoding
text, encoded, count = "aaabbccccd", [], 1
for i in range(1, len(text) + 1):
    if i < len(text) and text[i] == text[i-1]:
        count += 1
    else:
        encoded.append(text[i-1] + str(count)); count = 1
print("9.", "".join(encoded))

# 10. Longest substring without repeating characters
text, left, seen, best = "abcabcbb", 0, {}, 0
for right, c in enumerate(text):
    if c in seen and seen[c] >= left:
        left = seen[c] + 1
    seen[c] = right
    best = max(best, right - left + 1)
print("10. Longest unique substring:", best)
