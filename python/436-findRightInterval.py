# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        re = [-1 for i in intervals]
        order = []
        for i in range(len(intervals)):
            inter = intervals[i]
            order.append((inter.start, 1, i))
            order.append((inter.end, 0, i))
        order.sort()
        #print order
        stack = []
        for inter in order:
            if inter[1] == 0:
                stack.append(inter)
            else:
                for n in stack:
                    re[n[2]] = inter[2]
                stack = []
        return re
