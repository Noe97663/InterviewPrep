# given an array of nums
# return an array of nums, where each index position is the product
# of all other indices except the index itself

## Brute force - nested loop - O(n^2), O(1)
##             output array not considered in space analysis
## Using division - one loop, then a loop to divide - O(n), O(1)
## Prefix + Postfix array = result array - O(n), O(1) if you use the
##                          result array to do the math


def productExceptSelf(nums: list[int]) -> list[int]:
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
