class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        base = nums[len(nums) / 2]
        return sum(abs(num - base) for num in nums)
