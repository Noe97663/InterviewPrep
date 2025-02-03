# You are given an integer array nums where each element nums[i]
# indicates your maximum jump length at that position.
# Return true if you can reach the last index starting from
# index 0.

## Brute force - DFS for every possible jump - O(n!),O(n)
## DP - O(n^2), O(n)
## Greedy - start from the goal, iterate back
#           see if the goal is reachable, reset goal
#           - O(n), O(1)


# greedy
def canJump(nums: List[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


# bottom up DP
def canJump(nums: List[int]) -> bool:
    n = len(nums)
    dp = [False] * n
    dp[-1] = True

    for i in range(n - 2, -1, -1):
        end = min(n, i + nums[i] + 1)
        for j in range(i + 1, end):
            if dp[j]:
                dp[i] = True
                break
    return dp[0]


# brute force
def canJump(nums: List[int]) -> bool:
    def dfs(i):
        if i == len(nums) - 1:
            return True
        end = min(len(nums) - 1, i + nums[i])
        for j in range(i + 1, end + 1):
            if dfs(j):
                return True
        return False

    return dfs(0)
