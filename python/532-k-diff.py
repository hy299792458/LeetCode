class Solution(object):
    def findPairs(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        if k == 0:
            return sum(1 for t in count.values() if t > 1)
        elif k < 0:
            return 0
        re = 0
        for num in count:
            if num + k in count:
                re += 1
        return re
