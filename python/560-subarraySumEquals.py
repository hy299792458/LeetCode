class Solution(object):
    def subarraySum(self, nums, k):
        position = {}
        temp = 0
        re = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp == k:
                re += 1
            re += position.get(temp - k, 0)
            position[temp] = position.get(temp, 0) + 1
        return re
