class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        re = temp = 0
        for num in nums:
            if num:
                temp += 1
            else:
                re = max(temp, re)
                temp = 0
        return max(temp, re)
