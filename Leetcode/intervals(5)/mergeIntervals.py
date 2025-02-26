# merge intervals that overlap

## Sorting - sort the intervals by start, iterate through
##         - O(n. log n), O(1)


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda pair: pair[0])
    output = [intervals[0]]

    for start, end in intervals:
        lastEnd = output[-1][1]

        # combine intervals
        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    return output
