# Given an int array, find cont. sub-array  with
# largest product, return the product


## Brute force - all possible i,j - O(n^2), O(1)
## DP - Kadane's algo - keep running max and min going,
##      multiply curr num to max and min - O(n), O(1)
def maxProduct(nums: [int]) -> int:
    res = nums[0]
    curMin, curMax = 1, 1

    for num in nums:
        tmp = curMax * num
        # even if curMax becomes zero,
        # next iteration, curMax will be num
        curMax = max(num * curMax, num * curMin, num)
        curMin = min(tmp, num * curMin, num)
        res = max(res, curMax)
    return res
