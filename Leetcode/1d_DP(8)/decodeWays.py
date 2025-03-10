# find the number of ways a string of nums can be decoded into letters
# where A = 1, B = 2, Z = 26. leading zeroes are not valid
# 01 = 0 ways as the 0 cannot be parsed

## Brute force - recurse for every valid case - O(2^n), O(n)
## DP - top down - O(n), O(n)
##    - bottom up - O(n), O(n)

# bottom up - can be space optimized to O(1) since only 2 vals are used
def numDecodings(self, s: str) -> int:
    dp = {len(s): 1}
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i + 1 < len(s) and (s[i] == "1" or
            s[i] == "2" and s[i + 1] in "0123456"
        ):
            dp[i] += dp[i + 2]
    return dp[0]

def numDecodings(self, s: str) -> int:
    def dfs(i):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        # case of 1 num used
        res = dfs(i + 1)
        # case of 2 nums used
        if i < len(s) - 1:
            if (s[i] == '1' or 
                (s[i] == '2' and s[i + 1] < '7')):
                res += dfs(i + 2)

        return res

    return dfs(0)