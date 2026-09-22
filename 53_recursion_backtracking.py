# 57 Recursion and Backtracking - 11 practice programs

# 1 Factorial
def fact(n): return 1 if n<=1 else n*fact(n-1)
print("1 Factorial:",fact(5))
# 2 Fibonacci
def fib(n): return n if n<=1 else fib(n-1)+fib(n-2)
print("2 Fibonacci:",fib(7))
# 3 Recursive sum
def rsum(n): return 0 if n==0 else n+rsum(n-1)
print("3 Sum:",rsum(10))
# 4 Reverse string
def rev(s): return s if len(s)<=1 else rev(s[1:])+s[0]
print("4 Reverse:",rev("python"))
# 5 Palindrome
def pal(s): return len(s)<=1 or (s[0]==s[-1] and pal(s[1:-1]))
print("5 Palindrome:",pal("level"))
# 6 Subsets
def subsets(a):
    out=[]
    def bt(i,cur):
        if i==len(a):out.append(cur[:]);return
        bt(i+1,cur);cur.append(a[i]);bt(i+1,cur);cur.pop()
    bt(0,[]);return out
print("6 Subsets:",subsets([1,2,3]))
# 7 Permutations
def perms(a):
    out=[]
    def bt(i):
        if i==len(a):out.append(a[:]);return
        for j in range(i,len(a)):
            a[i],a[j]=a[j],a[i];bt(i+1);a[i],a[j]=a[j],a[i]
    bt(0);return out
print("7 Permutations:",perms([1,2,3]))
# 8 Combinations
def comb(a,k):
    out=[]
    def bt(i,cur):
        if len(cur)==k:out.append(cur[:]);return
        for j in range(i,len(a)):
            cur.append(a[j]);bt(j+1,cur);cur.pop()
    bt(0,[]);return out
print("8 Combinations:",comb([1,2,3,4],2))
# 9 Maze path
maze=[[0,0,1],[1,0,1],[0,0,0]]; path=[]
def maze_solve(r,c):
    if r<0 or c<0 or r>=len(maze) or c>=len(maze[0]) or maze[r][c] or (r,c) in path:return False
    path.append((r,c))
    if (r,c)==(2,2):return True
    if any(maze_solve(r+dr,c+dc) for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]):return True
    path.pop();return False
maze_solve(0,0);print("9 Maze:",path)
# 10 N-Queens
def queens(n):
    sol=[];cols=set();d1=set();d2=set();board=[["."]*n for _ in range(n)]
    def bt(r):
        if r==n:sol.append(["".join(x) for x in board]);return
        for c in range(n):
            if c in cols or r-c in d1 or r+c in d2:continue
            board[r][c]="Q";cols.add(c);d1.add(r-c);d2.add(r+c);bt(r+1)
            board[r][c]=".";cols.remove(c);d1.remove(r-c);d2.remove(r+c)
    bt(0);return sol
print("10 N-Queens(4) solutions:",len(queens(4)))
# 11 Word search
grid=[list("CAT"),list("XTO"),list("DOG")];word="CAT"
def exists(g,w):
    R,C=len(g),len(g[0])
    def bt(r,c,i):
        if i==len(w):return True
        if r<0 or c<0 or r>=R or c>=C or g[r][c]!=w[i]:return False
        ch=g[r][c];g[r][c]="#"
        ok=any(bt(r+dr,c+dc,i+1) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)])
        g[r][c]=ch;return ok
    return any(bt(r,c,0) for r in range(R) for c in range(C))
print("11 Word search:",exists(grid,word))
