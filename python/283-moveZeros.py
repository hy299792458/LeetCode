class Solution(object):
    def moveZeroes(self, nums):
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p2]:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        while p1 < len(nums):
            nums[p1] = 0
            p1 += 1
