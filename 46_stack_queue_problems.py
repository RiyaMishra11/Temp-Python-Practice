# Day 12 - 46: Stack and Queue Problems
from collections import deque

# 1. Stack push/pop
stack = []
stack.append(10); stack.append(20); stack.append(30)
print("1. Stack:", stack, "Pop:", stack.pop())

# 2. Reverse a string using stack
def reverse_string(text):
    stack = list(text)
    return "".join(stack.pop() for _ in range(len(stack)))
print("2.", reverse_string("Python"))

# 3. Balanced parentheses
def balanced(text):
    pairs = {")":"(", "]":"[", "}":"{"}
    stack = []
    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
print("3.", balanced("{[()]}"))

# 4. Queue using deque
q = deque([10, 20, 30])
print("4. Queue pop:", q.popleft())

# 5. Generate binary numbers
def binary_numbers(n):
    q = deque(["1"])
    result = []
    for _ in range(n):
        x = q.popleft()
        result.append(x)
        q.append(x+"0"); q.append(x+"1")
    return result
print("5.", binary_numbers(6))

# 6. Next greater element
def next_greater(a):
    result = [-1] * len(a)
    stack = []
    for i, x in enumerate(a):
        while stack and a[stack[-1]] < x:
            result[stack.pop()] = x
        stack.append(i)
    return result
print("6.", next_greater([4, 5, 2, 10, 8]))

# 7. Remove adjacent duplicates
def remove_adjacent(text):
    stack = []
    for ch in text:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
print("7.", remove_adjacent("abbaca"))

# 8. Evaluate postfix expression
def postfix(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append({"+":a+b, "-":a-b, "*":a*b, "/":a//b}[token])
    return stack[-1]
print("8.", postfix(["2", "3", "+", "4", "*"]))

# 9. Min stack
class MinStack:
    def __init__(self):
        self.data, self.minimum = [], []
    def push(self, x):
        self.data.append(x)
        self.minimum.append(x if not self.minimum else min(x, self.minimum[-1]))
    def pop(self):
        self.minimum.pop()
        return self.data.pop()
    def get_min(self):
        return self.minimum[-1]

ms = MinStack()
for x in [5, 2, 7, 1]: ms.push(x)
print("9. Min:", ms.get_min())

# 10. Circular queue simulation
class CircularQueue:
    def __init__(self, size):
        self.q, self.size = deque(), size
    def enqueue(self, x):
        if len(self.q) < self.size:
            self.q.append(x); return True
        return False
    def dequeue(self):
        return self.q.popleft() if self.q else None

cq = CircularQueue(3)
print("10.", cq.enqueue(1), cq.enqueue(2), cq.enqueue(3), cq.enqueue(4), cq.dequeue())
