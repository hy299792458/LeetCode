class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        maxPro = minPro = nums[0]
        res = maxPro
        for num in nums[1:]:
            maxPro, minPro = max(maxPro * num, minPro * num, num), min(maxPro * num, minPro * num, num)
            res = max(res, maxPro)
        return res
