# jump game but minimize the number of jumps

## brute force recursion - O(n!), O(n)
## DP - O(n^2), O(n)
## greed - O(n), O(1)

def jump(nums: [int]) -> int:
    res = 0
    l = r = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        res += 1
    return res