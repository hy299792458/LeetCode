class Solution(object):
    def trailingZeroes(self, n):
        res = 0
        temp = 5
        while temp <= n:
            res += n / temp
            temp *= 5
        return res
