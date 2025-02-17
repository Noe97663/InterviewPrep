# Find the minimum num of days to schedule all meetings
# given the start and end times


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


## two pointers - keep track of start times and end times in two arrays,
##                keep track of concurrent meetings, by iterating through
##                and checking if a meeting ends or starts - O(n. log n), O(n)
## many solutions with the same time and space complexity exist


def minMeetingRooms(intervals: [Interval]) -> int:
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res = count = 0
    s = e = 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res
