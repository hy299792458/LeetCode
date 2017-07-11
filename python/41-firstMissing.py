class Solution(object):
    def firstMissingPositive(self, nums):
        l = len(nums)
        for num in nums:
            temp = int(num) - 1
            if 0 <= temp < l:
                nums[temp] = float(nums[temp])
        for i in range(l):
            if type(nums[i]) == int:
                return i + 1
        return l + 1
