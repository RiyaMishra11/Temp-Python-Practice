# Day 10 - 38: Dynamic Programming

# 1. Fibonacci - bottom-up DP
n = 10
dp = [0, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
print("1. Fibonacci:", dp[n])

# 2. Fibonacci - memoization
from functools import lru_cache
@lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print("2. Memoized Fibonacci:", fib(10))

# 3. Climbing stairs
n = 6
ways = [0] * (n + 1)
ways[0] = ways[1] = 1
for i in range(2, n + 1):
    ways[i] = ways[i-1] + ways[i-2]
print("3. Climbing stairs:", ways[n])

# 4. Minimum cost to reach end
cost = [10, 15, 20, 5, 8]
dp = [0] * len(cost)
dp[0], dp[1] = cost[0], cost[1]
for i in range(2, len(cost)):
    dp[i] = cost[i] + min(dp[i-1], dp[i-2])
print("4. Minimum cost:", min(dp[-1], dp[-2]))

# 5. 0/1 Knapsack
weights, values, capacity = [2, 3, 4], [4, 5, 7], 5
dp = [0] * (capacity + 1)
for w, v in zip(weights, values):
    for c in range(capacity, w - 1, -1):
        dp[c] = max(dp[c], dp[c-w] + v)
print("5. Knapsack:", dp[capacity])

# 6. Minimum coins
coins, amount = [1, 3, 4], 6
dp = [float("inf")] * (amount + 1)
dp[0] = 0
for x in range(1, amount + 1):
    for coin in coins:
        if coin <= x:
            dp[x] = min(dp[x], dp[x-coin] + 1)
print("6. Minimum coins:", dp[amount])

# 7. Longest Common Subsequence
a, b = "abcde", "ace"
dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print("7. LCS:", dp[-1][-1])

# 8. Longest Increasing Subsequence
arr = [10, 9, 2, 5, 3, 7, 101, 18]
dp = [1] * len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print("8. LIS:", max(dp))

# 9. House Robber
money = [2, 7, 9, 3, 1]
prev2 = prev1 = 0
for amount in money:
    prev2, prev1 = prev1, max(prev1, prev2 + amount)
print("9. House Robber:", prev1)

# 10. Maximum subarray sum
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current = best = arr[0]
for x in arr[1:]:
    current = max(x, current + x)
    best = max(best, current)
print("10. Max subarray:", best)
