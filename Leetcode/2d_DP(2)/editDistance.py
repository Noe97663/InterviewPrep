# edit distance between 2 strings
# operations: insert, delete, replace

## Brute force - recurse into every possible combination
##             - O( 3^(m+n) ), O(m+n)
## DP - top down - memoizing brute force
##    - bottom up - make grid, fill grid - O(m. n), O(m. n)


# bottom up
def minDistance(self, word1: str, word2: str) -> int:
    dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    for j in range(len(word2) + 1):
        dp[len(word1)][j] = len(word2) - j
    for i in range(len(word1) + 1):
        dp[i][len(word2)] = len(word1) - i

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
    return dp[0][0]


# brute force
def minDistance(self, word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    def dfs(i, j):
        if i == m:
            return n - j
        if j == n:
            return m - i
        if word1[i] == word2[j]:
            return dfs(i + 1, j + 1)
        res = min(dfs(i + 1, j), dfs(i, j + 1))
        # different from earlier if, since we add 1 to dfs call
        res = min(res, dfs(i + 1, j + 1))
        return res + 1

    return dfs(0, 0)
