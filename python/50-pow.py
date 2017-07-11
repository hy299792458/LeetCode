class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sign = n < 0
        n = abs(n)
        temp = x
        re = 1
        while n:
            if n % 2:
                re *= temp
            temp *= temp
            n /= 2
        return 1 / re if sign else re
