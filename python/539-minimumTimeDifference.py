class Solution(object):
    def findMinDifference(self, timePoints):
        def convert(time):
            h, m = time.split(':')
            return int(h) * 60 + int(m)
        time = map(convert, timePoints)
        time.sort()
        re = float('inf')
        for i in range(len(time)):
            re = min(re, (time[i]- time[i-1]) % 1440)
        return re
