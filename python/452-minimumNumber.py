class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        cnt = 0
        points.sort(key = lambda x: [x[1], x[0]])
        end = points[0][1]
        cnt = 1
        for p in points[1:]:
            if end < p[0]:
                cnt += 1
                end = p[1]
        return cnt
