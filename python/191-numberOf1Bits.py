class Solution(object):
    def hammingWeight(self, n):
        re = 0
        while n:
            re += n % 2
            n /= 2
        return re
