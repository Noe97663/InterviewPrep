# insert an interval, combining overlapping intervals if necessary

## Linear search - O(n), O(1)


def insert(intervals: [[int]], newInterval: [int]) -> [[int]]:
    n = len(intervals)
    i = 0
    res = []

    # end times do not overlap with new start time
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    # if i exists, intervals[i] is the earliest overlapping
    if i < n:
        newInterval[0] = min(newInterval[0], intervals[i][0])
    # while the intervals are still inside the end time of the new insertion
    while i < n and newInterval[1] >= intervals[i][0]:
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    # insert the new interval
    res.append(newInterval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res
