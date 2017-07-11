class Solution(object):
    def removeElement(self, nums, val):
        l = r = 0
        length = len(nums)
        while r < length:
            if nums[r] == val:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l
