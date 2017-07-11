class Solution(object):
    def removeDuplicates(self, nums):
        p1, p2 = 0, 1
        if not nums:
            return 0
        while p2 < len(nums):
            if nums[p2] == nums[p1]:
                p2 += 1
            else:
                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1
        return p1 + 1
