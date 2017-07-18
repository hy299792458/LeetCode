class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total / 2
        reach = set([0])
        for num in nums:
            newReach = set()
            for seen in reach:
                newReach.add(seen + num)
            reach |= newReach
            if target in reach:
                return True
        return False
