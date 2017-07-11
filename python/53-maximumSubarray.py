class Solution(object):
    def maxSubArray(self, nums):
        re = temp = nums[0]
        for num in nums[1:]:
            temp = max(temp + num, num)
            re = max(re, temp)
        return re
