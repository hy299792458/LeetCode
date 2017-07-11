class Solution(object):
    def totalHammingDistance(self, nums):
        count = {}
        for num in nums:
            temp = num
            i = 0
            while temp:
                count[i] = count.get(i, 0) + temp % 2
                temp /= 2
                i += 1
        l = len(nums)
        re = 0
        i = 0
        while i in count:
            re += (l - count[i]) *count[i]
            i += 1
        return re
