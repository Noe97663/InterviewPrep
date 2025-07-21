# given a grid of m*n
# find the number of unique paths from the top left to the bottom right
# can only move right or down

# brute force - just recurse lool xD - O(2^(m+n)), O(m+n)
# top down dp - memoizise brute force - O(m*n), O(m*n)
# bottom up dp - start from end, go left and up - O(m*n), O(m*n)
# space optimize - only use two rows (curr and below)
#                - OR just use one column - O(m*n), O(n)

# brute force
def uniquePaths(self, m: int, n: int) -> int:
        
    def dfs(i, j):
        if i == (m - 1) and j == (n - 1):
            return 1
        if i >= m or j >= n:
            return 0
        return dfs(i, j + 1) + dfs(i + 1, j)
    
    return dfs(0, 0)

# unoptimized bottom up
def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[m - 1][n - 1] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

    return dp[0][0]