class Solution(object):
    def rob1(self, nums):
        i = len(nums) - 1
        nums += [0, 0]
        while i >= 0:
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
            i -= 1
        return nums[0]
    
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
