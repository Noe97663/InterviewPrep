# find the number in the array that is not repeated
# must be O(1) space

# could loop twice for O(1) space
# could use set for O(n) time and space

# sort in place - O(n. log n), O(1)
# XOR - ^ -  O(n), O(1)

def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res = num ^ res
    return res