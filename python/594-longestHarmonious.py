class Solution(object):
    def findLHS(self, nums):
        count = {}
        re = (0, 0, 0)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for k in count:
            if k + 1 in count:
                re = max(re, (count[k] + count[k + 1], k, k + 1))
        return re[0]
