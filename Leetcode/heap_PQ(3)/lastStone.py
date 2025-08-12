# given array of stone weights, smash stones together till (n)one left
# if weights equal, both gone. Else, big-small

# sort - sort once, use 2nd array to reorder after crushing
#      - O(n^2), O(n)
# heap - O(n. log n), O(n)

import heapq
# python heaps are min heaps by default
# * -1 to use min as max heap
def lastStoneWeight(self, stones: [int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)

    stones.append(0)
    return abs(stones[0])