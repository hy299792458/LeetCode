class Solution(object):
    def PredictTheWinner(self, nums):
        store = {}
        def dp(i,j):
            if (i, j) in store:
                return store[(i,j)]
            if i >= j:
                temp = nums[i]
            else:
                temp = max(nums[i] - dp(i + 1,j), nums[j] - dp(i, j -1))
            store[(i,j)] = temp
            return temp
        return dp(0, len(nums) - 1) >= 0
