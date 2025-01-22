# Return triplets of numbers from the array that equal 0

## Brute force - nested loop - O(n^3), O(1)
##
## Sorting makes a huge hit on runtime, so why not
## Optimal - Sort the array
##           2 sum for the rest of the array - O(n^2), O(1)
##           Note: 2 sum can be solved with 2 pointers here
##                 due to the sorted array


def threeSum(nums: list[int]) -> list[list[int]]:
    out = []
    nums = sorted(nums)
    i = 0
    while i < len(nums):
        target = nums[i] * -1
        L = i + 1
        R = len(nums) - 1
        while L < R:
            if (nums[L] + nums[R]) == target:
                out.append([nums[i], nums[L], nums[R]])
                while (L + 1) < len(nums) and nums[L] == nums[L + 1]:
                    L += 1
                L += 1
                R -= 1
            elif (nums[L] + nums[R]) < target:
                L += 1
            else:
                R -= 1

        while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return out
