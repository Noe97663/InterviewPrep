# A sorted array has been rotated,
# find the minimum

## Brute force - O(n), O(1)
## Binary Search- O(log n), O(1)


def findMin(nums: list[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        m = (l + r) // 2
        res = min(res, nums[m])
        # num on left is smaller, correct, look in right
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res
