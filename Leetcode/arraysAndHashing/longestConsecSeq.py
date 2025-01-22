# Find the longest consecutive sequence of ints in a jumbled array

## Sort - iterate through - O(n. log n), O(1)
## HashSet - start iterating through a sequence using the set
##           if you found a number which is the start of a sequence
#            [ (n-1) not present ], O(n), O(n)


def longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if (num - 1) not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
