class Solution(object):
    def productExceptSelf(self, nums):
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(2, len(nums) + 1):
            right[-i] = right[-i + 1] * nums[- i + 1]
        return [a* b for a, b in zip(left,right)]
