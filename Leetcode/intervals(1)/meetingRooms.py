# given tuples of meetings times (start,end)
# check if they have conflicts

## Brute force - check each meeting against every other
##               - O(n^2), O(1)
## Sort - sort meetings by start, iterate through,
##        checking if one starts before prev ends
##        - O(n logn), O(1)


def canAttendMeetings(intervals: [tuple()]) -> bool:
    intervals.sort(key=lambda i: i.start)

    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        if i1.end > i2.start:
            return False
    return True
