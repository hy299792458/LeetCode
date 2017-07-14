# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        end = float('-inf')
        res = 0
        for inter in sorted(intervals, key=lambda i: i.end):
            if inter.start >= end:
                end = inter.end
            else:
                res += 1
        return res
