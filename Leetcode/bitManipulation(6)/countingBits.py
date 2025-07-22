# count the 1 bits of each number
# 3 ---> 2

## Brute force - repeatedly / and %  (or << and &) to get the number of
##               1's in the num (log_2 n times) - O(logn), O(n)
## Optimal - using n & n-1 to remove a 1 bit from the representation
##         - O(1 bits), O(1)


def hammingWeight(n: int) -> int:
    res = 0
    while n:
        # removes 1 1-bit
        n = n & n - 1
        res += 1
    return res
