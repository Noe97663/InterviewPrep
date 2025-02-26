# Find the minimum num of rooms to schedule all meetings
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
    s_i = e_i = 0
    while s_i < len(intervals):
        if start[s_i] < end[e_i]:
            s_i += 1
            count += 1
        else:
            e_i += 1
            count -= 1
        res = max(res, count)
    return res
