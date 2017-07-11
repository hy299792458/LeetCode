class Solution(object):
    def sortColors(self, nums):
        count = {0: 0, 1: 0, 2: 0}
        for num in nums:
            count[num] += 1
        nums[:] = [0] * count[0] + [1] * count[1] + [2] * count[2]
