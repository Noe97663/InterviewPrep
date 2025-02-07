# find the sub-array sum that is maximum

## Brute force - sum every possible A[i,j] - O(n^2), O(1)
## Kadane's algorithm - O(n), O(1)


def maxSubArray(nums: [int]) -> int:
    maxSub, curSum = nums[0], 0
    for num in nums:
        if curSum < 0:
            curSum = 0
        curSum += num
        maxSub = max(maxSub, curSum)
    return maxSub
