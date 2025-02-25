# Find the length of the longest increasing subsequence
# given an array of nums

## Brute force - Recurse on every choice - O(2^n), O(n)
## DP - top down - memoize brute force
##    - bottom up - start from the smallest possible case
##      build from there - O(n^2), O(n)


# bottom up
def lengthOfLIS(nums: [int]) -> int:
    LIS = [1] * len(nums)
    # start points
    for i in range(len(nums) - 1, -1, -1):
        # end points
        for j in range(i + 1, len(nums)):
            # if the sequence is possible
            if nums[i] < nums[j]:
                # max(max so far, new sequence)
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)


# brute force
def lengthOfLIS(nums: [int]) -> int:
    def dfs(i, j):
        if i == len(nums):
            return 0
        # not include
        LIS = dfs(i + 1, j)

        # include
        if j == -1 or nums[j] < nums[i]:
            LIS = max(LIS, 1 + dfs(i + 1, i))

        return LIS

    return dfs(0, -1)
