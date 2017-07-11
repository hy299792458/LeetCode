class Solution(object):
    def findPeakElement(self, nums):
        nums = [-float('inf')] + nums + [-float('inf')]
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i - 1
