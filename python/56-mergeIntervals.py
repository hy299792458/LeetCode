# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        res = []
        intervals.sort(key = lambda x: [x.start, x.end])
        for inter in intervals:
            if res and res[-1].end >= inter.start:
                temp = res.pop()
                res.append(Interval(min(temp.start, inter.start), max(temp.end, inter.end)))
            else:
                res.append(inter)
        return res
