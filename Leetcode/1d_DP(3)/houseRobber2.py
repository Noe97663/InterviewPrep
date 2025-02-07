# given an array of house values (THE ARRAY LOOPS)
# need to maximize robbed house values
# but cannot rob adjacent houses

## Brute force - either I do or I don't, find the maximizing choice
##             - O(2^n), O(n)
## DP - top down is memoized brute force
##      bottom up is novel and can be space optimized
##      - O(n), O(n)
## Space optimized DP - O(n), O(1)


# solve house robber 1 in two cases, without index 0 and without index -1
def rob(nums: [int]) -> int:
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


def helper(nums):
    rob1, rob2 = 0, 0

    for num in nums:
        newRob = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2


# memoized brute force
def rob(nums: [int]) -> int:
    if len(nums) == 1:
        return nums[0]
    # stores 2 numbers, True(1) for pairs starting at 0
    #                   False(0) for pairs starting at 1
    memo = [[-1] * 2 for _ in range(len(nums))]

    def dfs(i, flag):
        if i >= len(nums) or (flag and i == len(nums) - 1):
            return 0
        if memo[i][flag] != -1:
            return memo[i][flag]
        memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))
        return memo[i][flag]

    return max(dfs(0, True), dfs(1, False))


# brute force
def rob(nums: [int]) -> int:
    if len(nums) == 1:
        return nums[0]

    # flag helps to stop recursing too far if you started at 0
    def dfs(i, flag):
        if i >= len(nums) or (flag and i == len(nums) - 1):
            return 0

        return max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))

    return max(dfs(0, True), dfs(1, False))
