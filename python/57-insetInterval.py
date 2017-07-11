# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        l, r = newInterval.start, newInterval.end
        left = l
        right = r
        lint = len(intervals)
        i = 0
        while i < lint and intervals[i].end < l:
            res.append(intervals[i])
            i += 1
        while i < lint and intervals[i].start <= r:
            left = min(left, intervals[i].start)
            right = max(right, intervals[i].end)
            i += 1
        res.append(Interval(left, right))
        res += intervals[i:]
        return res
