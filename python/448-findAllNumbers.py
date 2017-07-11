class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            pos = abs(num) - 1
            nums[pos] = -abs(nums[pos])
        return [(i + 1) for i in range(len(nums)) if nums[i] > 0]
