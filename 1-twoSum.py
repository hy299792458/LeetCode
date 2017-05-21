class Solution(object):
    def twoSum(self, nums, target):
        used = {}
        for i in range(len(nums)):
            if nums[i] in used:
                return [i, used[nums[i]]]
            else:
                used[target - nums[i]] = i
