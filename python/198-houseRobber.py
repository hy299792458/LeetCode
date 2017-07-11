class Solution(object):
    def rob(self, nums):
        i = len(nums) - 1
        nums += [0, 0]
        while i >= 0:
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
            i -= 1
        return nums[0]
