class Solution(object):
    def checkSubarraySum(self, nums, k):
        k = abs(k)
        temp = 0
        pos = {0: -1}
        for i in range(len(nums)):
            temp += nums[i]
            if k > 0:
                temp %= k 
            if temp in pos:
                if pos[temp] < i - 1:
                    return True
            else:
                pos[temp] = i
        return False
