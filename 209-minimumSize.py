class Solution(object):
    def minSubArrayLen(self, s, nums):
        l = r = 0
        temp = 0
        res = float('inf')
        while r < len(nums):
            while r < len(nums) and temp < s:
                temp += nums[r]
                r += 1
            if temp < s:
                break
            while l <= r and temp >= s:
                temp -= nums[l]
                l += 1
            res = min(res, r - l + 1)
        return res if res < float('inf') else 0
