# remove intervals that overlap

## Brute force - consider deleting every interval in every case
##             - O(2^n), O(n)
## Sorting - sort the intervals by start, iterate through, remove
##           the interval that ends the latest - O(n. log n), O(1)


def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
    intervals.sort()
    res = 0
    prevEnd = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res
