# check if array has duplicate - Time, Space Complexity
# (72 characters per line)

## Brute force - nested loop - O(n^2), O(1)
## Sorted array - O (n log n), O(1)
## Hashmap - O(n), O(n)


def hasDuplicate(nums) -> bool:
    s = set()
    for n in nums:
        # found duplicate
        if n in s:
            return True
        s.add(n)
    return False


print(hasDuplicate([1, 2, 4, 5, 11]))
