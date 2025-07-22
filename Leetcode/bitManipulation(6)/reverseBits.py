# reverse bits in a 32-bit int

## Brute force - make a string version of the integer after
##              / and % repeatedly, reverse that and make it an int
##              - O(1), O(1)
## Bit Manipulation - use >> (or <<) and + - O(1), O(1)


def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res += bit << (31 - i)
    return res
