# given a list of ints, and groupsize k 
# check if you can make k-sized groups of consecutive ints

# brute force - sort and use a hashmap to count groups 
#             - O(n log n), O(n)
# greedy - always start at the smallest int, count groups using hashmap
#        - O(n), O(n)

# Why is this O(n) with the nested loops?
# Consider starting at 9 in [1,2,3,4,5,6,7,8,9]
# After counting all the way back to 1, we only count up
# to 9, we run through the array twice - O(2n) = O(n)

from collections import Counter

def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize:
        return False

    count = Counter(hand)
    for num in hand:
        start = num
        while count[start - 1]:
            start -= 1
        while start <= num:
            while count[start]:
                for i in range(start, start + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
            start += 1
    return True