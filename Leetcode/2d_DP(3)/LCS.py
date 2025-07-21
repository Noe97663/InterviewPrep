# longest common subsequence between 2 words


## Brute force - recurse with every choice, find max
##             - O( 2^(n+m) ), O(m+n)
## DP - top down, memoize - O(m. n), O(m. n)
## DP - bottom up - O(m. n), O(m, n) - can still optimize for space


# bottom up
def longestCommonSubsequence(text1: str, text2: str) -> int:
    # initialize grid
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    # start from bottom left corner
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            # same letter
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]


# brute force
def longestCommonSubsequence(text1: str, text2: str) -> int:
    def dfs(i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + dfs(i + 1, j + 1)
        return max(dfs(i + 1, j), dfs(i, j + 1))

    return dfs(0, 0)
