class Solution(object):
    def maxCount(self, m, n, ops):
        minx, miny = m, n
        for x, y in ops:
            minx = min(minx, x)
            miny = min(miny, y)
        return minx * miny
