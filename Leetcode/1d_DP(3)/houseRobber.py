# given an array of house values
# need to maximize robbed house values
# but cannot rob adjacent houses

## Brute force - either I do or I don't, find the maximizing choice
##             - O(2^n), O(n)
## DP - top down is memoized brute force
##      bottom up is novel and can be space optimized
##      - O(n), O(n)
## Space optimized DP - O(n), O(1)


# space optimized bottom up
def rob(nums: [int]) -> int:
    # rob curr-1 pairs, rob curr + curr-2 pairs,
    rob1, rob2 = 0, 0
    for num in nums:
        # so you add curr to last iteration's curr-1 pairs
        temp = max(num + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


# bottom up
def rob(nums: [int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        # I rob previous house pairs, or curr house pairs
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]


# memoized brute force - top down DP
def rob(nums: [int]) -> int:
    memo = [-1] * len(nums)

    def dfs(i):
        if i >= len(nums):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
        return memo[i]

    return dfs(0)


# brute force
def rob(nums: [int]) -> int:
    def dfs(i):
        if i >= len(nums):
            return 0
        # don't rob curr, do rob curr
        return max(dfs(i + 1), nums[i] + dfs(i + 2))

    return dfs(0)
