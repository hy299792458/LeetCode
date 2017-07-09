class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dp[j])
            dp[i] = res + 1
        return max(dp)
