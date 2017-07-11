class Solution(object):
    def findDuplicate(self, nums):
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            nums[abs(num)] *= -1
