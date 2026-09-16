# Day 7 - 27: Stack and Queue Data Structures
from collections import deque

def create_stack():  # 1. Create stack
    return ["A","B","C"]

def push(stack, item):  # 2. Push item
    stack.append(item)

def pop_item(stack):  # 3. Pop item
    return stack.pop() if stack else None

def peek(stack):  # 4. Peek top
    return stack[-1] if stack else None

def reverse_string(text):  # 5. Reverse using stack
    stack=list(text); result=[]
    while stack: result.append(stack.pop())
    return "".join(result)

def balanced_parentheses(text):  # 6. Balanced brackets
    stack=[]; pairs={")":"(", "]":"[", "}":"{"}
    for c in text:
        if c in "([{": stack.append(c)
        elif c in ")]}" and (not stack or stack.pop()!=pairs[c]): return False
    return not stack

def create_queue():  # 7. Create queue
    return deque(["A","B","C"])

def enqueue(queue, item):  # 8. Enqueue
    queue.append(item)

def dequeue_item(queue):  # 9. Dequeue
    return queue.popleft() if queue else None

def binary_numbers(n):  # 10. Generate binary numbers using queue
    q=deque(["1"]); result=[]
    for _ in range(n):
        value=q.popleft(); result.append(value)
        q.append(value+"0"); q.append(value+"1")
    return result

if __name__ == "__main__":
    stack=create_stack(); push(stack,"D")
    print(stack, pop_item(stack), peek(stack))
    print(reverse_string("Python"))
    print(balanced_parentheses("{[()]}"))
    queue=create_queue(); enqueue(queue,"D")
    print(list(queue), dequeue_item(queue))
    print(binary_numbers(8))
