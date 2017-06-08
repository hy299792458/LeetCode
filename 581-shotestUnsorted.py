class Solution(object):
    def findUnsortedSubarray(self, nums):
        order = sorted(nums)
        l, r = 0, len(nums) - 1
        try:
            while order[l] == nums[l]:
                l += 1
            while order[r] == nums[r]:
                r -= 1
            return r - l + 1
        except:
            return 0
