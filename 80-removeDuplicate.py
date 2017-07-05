class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        l = r = 2
        while r < len(nums):
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1
                r += 1
            else:
                r += 1
        return l
