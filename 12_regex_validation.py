# Python Practice - Regular Expressions
import re

# 1. Only digits
s=input("Text: "); print(bool(re.fullmatch(r"\d+",s)))

# 2. Only alphabets
s=input("Text: "); print(bool(re.fullmatch(r"[A-Za-z]+",s)))

# 3. Validate email
s=input("Email: "); print(bool(re.fullmatch(r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}",s)))

# 4. Validate Indian mobile number
s=input("Mobile: "); print(bool(re.fullmatch(r"[6-9]\d{9}",s)))

# 5. Extract numbers
s=input("Sentence: "); print(re.findall(r"\d+",s))

# 6. Extract capitalized words
s=input("Sentence: "); print(re.findall(r"\b[A-Z][a-z]*\b",s))

# 7. Remove extra spaces
s=input("Text: "); print(re.sub(r"\s+"," ",s).strip())

# 8. Check password
s=input("Password: ")
ok=len(s)>=8 and re.search(r"[A-Z]",s) and re.search(r"[a-z]",s) and re.search(r"\d",s)
print("Strong" if ok else "Weak")

# 9. Extract hashtags
s=input("Post: "); print(re.findall(r"#\w+",s))

# 10. Extract dates
s=input("Text with dates: "); print(re.findall(r"\b\d{2}-\d{2}-\d{4}\b",s))
