class Solution(object):
    def minMoves(self, nums):
        base = min(nums)
        return sum(num - base for num in nums)
