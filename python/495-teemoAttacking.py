class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        end = timeSeries[0] + duration
        re = duration
        for time in timeSeries[1:]:
            if end <= time:
                re += duration
            else:
                re += duration - (end - time)
            end = time + duration
        return re
