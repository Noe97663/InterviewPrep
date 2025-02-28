# n stairs, can take either 1 or 2 steps
# how many distinct ways to climb stairs?

## Brute force - recursive calls of all permutations - O(2^n),O(n)
## DP top down/bottom up - O(n), O(n)
## Space optimized - O(n), O(1)
## Optimal - math heavy - O(log n), O(1)


# Space optimized bottom up
def climbStairs(n: int) -> int:
    # one is one step back
    # two is two steps back
    # add them together - two possible ways to get up
    # one step back is now the sum
    # two steps back is now (old) one step back
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


# bottom up
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# top down - brute force with memoization
def climbStairs(n: int) -> int:
    cache = [-1] * n

    def dfs(i):
        if i >= n:
            return i == n
        # memoization
        if cache[i] != -1:
            return cache[i]
        cache[i] = dfs(i + 1) + dfs(i + 2)
        return cache[i]

    return dfs(0)
