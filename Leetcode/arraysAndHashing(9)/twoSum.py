# Find the indices of the pair of elements that sum to target value

## Nested loop strategy - O(n^2), O(1)
## One pass using hashmap - O(n), O(n)


def twoSum(nums: list[int], target: int) -> list[int]:
    dict = {}
    for index in range(len(nums)):
        n = nums[index]
        need = target - n
        # solution found
        if need in dict:
            return [dict[need], index]
        else:
            dict[n] = index
