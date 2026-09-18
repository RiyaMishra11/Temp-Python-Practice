# Day 10 - 37: Hashing & Frequency Maps

# 1. Frequency of numbers
nums = [2, 3, 2, 5, 3, 2, 7]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
print("1.", freq)

# 2. Character frequency
text = "programming"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("2.", freq)

# 3. First non-repeating character
text = "aabbcddee"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("3.", next((ch for ch in text if freq[ch] == 1), None))

# 4. Two Sum
nums, target = [2, 7, 11, 15], 9
seen, answer = {}, None
for i, n in enumerate(nums):
    if target - n in seen:
        answer = (seen[target - n], i)
        break
    seen[n] = i
print("4. Two Sum:", answer)

# 5. Remove duplicates preserving order
items = [4, 2, 4, 1, 2, 5, 1]
print("5.", list(dict.fromkeys(items)))

# 6. Find duplicates
items = [1, 2, 3, 2, 4, 5, 3, 6]
seen, duplicates = set(), set()
for x in items:
    if x in seen:
        duplicates.add(x)
    seen.add(x)
print("6.", sorted(duplicates))

# 7. Group words by first letter
words = ["apple", "ant", "banana", "ball", "cat"]
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
print("7.", groups)

# 8. Anagram check
print("8.", sorted("listen") == sorted("silent"))

# 9. Most frequent item
items = ["red", "blue", "red", "green", "blue", "red"]
freq = {}
for x in items:
    freq[x] = freq.get(x, 0) + 1
print("9.", max(freq, key=freq.get))

# 10. Word frequency
sentence = "python is easy and python is powerful"
freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1
print("10.", freq)
