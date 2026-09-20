# Day 12 - 48: Python Quiz Application Mini Project

questions = [
    {"q": "Which keyword defines a function?", "options": ["A. func", "B. def", "C. function", "D. define"], "answer": "B"},
    {"q": "Which type is [1, 2, 3]?", "options": ["A. tuple", "B. set", "C. list", "D. dict"], "answer": "C"},
    {"q": "Which symbol starts a comment?", "options": ["A. //", "B. #", "C. <!--", "D. **"], "answer": "B"},
    {"q": "What does len() return?", "options": ["A. Type", "B. Length", "C. Value", "D. Index"], "answer": "B"},
    {"q": "Which collection stores key-value pairs?", "options": ["A. list", "B. tuple", "C. dict", "D. set"], "answer": "C"},
    {"q": "Which loop repeats over items?", "options": ["A. for", "B. if", "C. def", "D. try"], "answer": "A"},
    {"q": "What is 2 ** 3?", "options": ["A. 6", "B. 8", "C. 9", "D. 12"], "answer": "B"},
    {"q": "Which method adds to a list?", "options": ["A. add()", "B. push()", "C. append()", "D. insertEnd()"], "answer": "C"},
    {"q": "Which value represents no value?", "options": ["A. null", "B. None", "C. empty", "D. void"], "answer": "B"},
    {"q": "Which module provides random numbers?", "options": ["A. math", "B. os", "C. random", "D. numbers"], "answer": "C"}
]

# 1. Count questions
print("1. Number of questions:", len(questions))

# 2. Display first question
print("2.", questions[0]["q"])

# 3. Display all options
print("3. Options:", questions[0]["options"])

# 4. Check one answer
answer = "B"
print("4. First answer correct:", answer == questions[0]["answer"])

# 5. Calculate score from answers
user_answers = ["B", "C", "B", "B", "C", "A", "B", "C", "B", "C"]
score = sum(a == q["answer"] for a, q in zip(user_answers, questions))
print("5. Score:", score)

# 6. Calculate percentage
percentage = score / len(questions) * 100
print("6. Percentage:", percentage)

# 7. Find wrong answers
wrong = [i+1 for i, (a, q) in enumerate(zip(user_answers, questions)) if a != q["answer"]]
print("7. Wrong question numbers:", wrong)

# 8. Pass/fail
print("8. Result:", "PASS" if percentage >= 50 else "FAIL")

# 9. Grade
grade = "A" if percentage >= 90 else "B" if percentage >= 75 else "C" if percentage >= 60 else "D" if percentage >= 50 else "F"
print("9. Grade:", grade)

# 10. Quiz summary
print("10. Summary:", {"score": score, "total": len(questions), "percentage": percentage, "grade": grade})
