# given denominations, minimize how many coins make target
# can pick a denomination more than once

## Brute force - DFS recursion - pick a coin, recurse on that choice
##             - O(n^t), O(t) - t = target, n = no. of denominations
## Top down DP - memoized brute force (table for repeated work, no call
##               for t<0 - O(n. t), O(t)
## Bottom up DP - how many coins for 1,2,3,4,...T Build an array for it,
##               use previous values to inform what should go in curr position
##              - O(n. t), O(t)


# bottom up DP
def coinChange(coins: [int], amount: int) -> int:
    # 5 * [5] = [ 0 , 5 , 5 , 5 , 5 ]
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != amount + 1 else -1


# Brute Force
def coinChange(coins: [int], amount: int) -> int:

    def dfs(amount):
        if amount == 0:
            return 0

        res = 1e9  # 1, 000, 000, 000
        for coin in coins:
            if amount - coin >= 0:
                res = min(res, 1 + dfs(amount - coin))
        return res

    minCoins = dfs(amount)
    return -1 if minCoins == 1e9 else minCoins
