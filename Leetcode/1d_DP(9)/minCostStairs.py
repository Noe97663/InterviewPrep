# given a cost array, where the cost of step i is A[i]
# find the min cost to get to the top, if you can take 
# 1 or 2 steps at a time (start at i = 0/1)

## brute - every possible choice recurse - O(2^n), O(n)
## DP - O(n), O(n)
## space optimized bottom up - O(n), O(1)

# bottom up - space optimized
def minCostClimbingStairs(cost: [int]) -> int:
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    return min(cost[0], cost[1])

# top down - memoized
def minCostClimbingStairs(self, cost: List[int]) -> int:
    memo = [-1] * len(cost)
    
    def dfs(i):
        if i >= len(cost):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        return memo[i]
    
    return min(dfs(0), dfs(1))

#brute force
def minCostClimbingStairs(cost: [int]) -> int:
    def dfs(i):
        if i >= len(cost):
            return 0
        return cost[i] + min(dfs(i + 1), dfs(i + 2))
    
    return min(dfs(0), dfs(1))