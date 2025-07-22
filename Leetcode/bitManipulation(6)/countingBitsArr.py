# in array of [0-n], count the 1 bits of each index number
# output - [0,1,1,2,1,2,2,3,1,..]

## Brute force - for i in n, repeatedly / and % to get the number of
##               1's in the num (log_2 n times) - O(n log n), O(n)
## DP - patterns repeat after MSB, bottom up DP - O(n), O(n)


def countBits(n: int) -> [int]:
    # initialize
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp
