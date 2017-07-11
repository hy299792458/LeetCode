class Solution(object):
    def missingNumber(self, nums):
        re = len(nums)
        for i in xrange(len(nums)):
            re ^= i
            re ^= nums[i]
        return re
