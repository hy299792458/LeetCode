class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        re = 0
        l1 = l2 = heaters[0]
        p = 1
        for h in houses:
            while l2 <= h and p < len(heaters):
                l2, l1 = heaters[p], l2
                p += 1
            re = max(re, min(abs(l2 - h), abs(l1 - h)))
        return re
