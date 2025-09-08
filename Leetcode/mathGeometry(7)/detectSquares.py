#Write a data structure that takes points in, counts squares possible with a point

# Brute force - nested loops  - O(n^3), O(n)
# Hashmap - loop to get diagonal point (x1-x2 == y2-y1),
#           check for points (x1,y2) and (x2,y1) - O(n^2), O(n)
#         - O(n), O(n)

from collections import defaultdict



class CountSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res