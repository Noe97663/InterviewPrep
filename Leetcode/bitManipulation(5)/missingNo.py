# range [0-n], but only n-1 spots in array
# find the missing number

## Brute force - sort array, start for loop,
##               if i!=Arr[i], - O(n logn), O(n)
## Hash set - use set to hash all arr nums,
##            for loop, if i not in set, BOOM
##            - O(n), O(n)
## Sum subtraction - sum of array minus sum of
#                    range - O(n), O(1)
## Bitwise XOR - XOR with the same number gives
##              0, loop through array, i XOR A[i]
##              final remaining number wont get
##              cancelled out - O(n), O(1)


# XOR solution
def missingNumber(nums: [int]) -> int:
    n = len(nums)
    xor = n
    for i in range(n):
        xor ^= i ^ nums[i]
    return xor
