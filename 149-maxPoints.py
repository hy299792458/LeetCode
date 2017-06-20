# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

#import numpy for more accuracy
class Solution(object):
    def maxPoints(self, points):
        import numpy
        re = 0
        for i in range(len(points)):
            slop = {}
            same = 1
            for j in range(i + 1, len(points)):
                if points[i].x == points[j].x:
                    if points[i].y != points[j].y:
                        slop['inf'] = slop.get('inf', 0) + 1
                    else:
                        same += 1
                else:
                    k = (points[i].y - points[j].y) * numpy.longdouble(1) / (points[i].x - points[j].x)
                    slop[k] = slop.get(k, 0) + 1
            re = max(max(slop.values() + [0]) + same, re)
        return re
