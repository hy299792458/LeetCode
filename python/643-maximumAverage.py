class Solution(object):
    def findMaxAverage(self, nums, k):
        res = sum(nums[:k])
        temp = res
        for i in range(k, len(nums)):
            temp += nums[i]
            temp -= nums[i - k]
            res = max(temp, res)
        return res * 1.0 / k
        
