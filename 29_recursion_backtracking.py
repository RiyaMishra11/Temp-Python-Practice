# Day 8 - 29: Recursion and Backtracking
def factorial(n):  # 1
    return 1 if n <= 1 else n * factorial(n-1)

def fibonacci(n):  # 2
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def recursive_sum(n):  # 3
    return 0 if n <= 0 else n + recursive_sum(n-1)

def digit_sum(n):  # 4
    n = abs(n)
    return n if n < 10 else n % 10 + digit_sum(n//10)

def reverse_string(s):  # 5
    return s if len(s) <= 1 else reverse_string(s[1:]) + s[0]

def is_palindrome(s):  # 6
    s = ''.join(c.lower() for c in s if c.isalnum())
    return len(s) <= 1 or (s[0] == s[-1] and is_palindrome(s[1:-1]))

def power(base, exp):  # 7
    return 1 if exp == 0 else base * power(base, exp-1)

def binary_strings(n, prefix=""):  # 8
    if n == 0:
        print(prefix)
        return
    binary_strings(n-1, prefix+"0")
    binary_strings(n-1, prefix+"1")

def permutations(items):  # 9
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path.copy())
            return
        for i, item in enumerate(remaining):
            path.append(item)
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    backtrack([], items)
    return result

def maze_path(maze, r=0, c=0, path=None):  # 10
    path = [] if path is None else path
    if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]) or maze[r][c] != 0:
        return None
    path.append((r,c))
    if (r,c) == (len(maze)-1, len(maze[0])-1):
        return path.copy()
    maze[r][c] = 2
    for dr, dc in ((1,0),(0,1),(-1,0),(0,-1)):
        ans = maze_path(maze, r+dr, c+dc, path)
        if ans: return ans
    maze[r][c] = 0
    path.pop()
    return None

if __name__ == "__main__":
    print(factorial(5), fibonacci(8), recursive_sum(10), digit_sum(12345))
    print(reverse_string("Python"), is_palindrome("Never odd or even"), power(2,8))
    binary_strings(3)
    print(permutations(["A","B","C"]))
    print(maze_path([[0,0,1],[1,0,1],[0,0,0]]))
