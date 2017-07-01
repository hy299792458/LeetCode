class Solution(object):
    def integerReplacement(self, n):
        res = 0
        while n:
            if n % 4 == 1 or n == 3:
                n -= 1
                res += 1
            elif n % 2 == 1:
                n += 1
                res += 1
            else:
                n /= 2
                res += 1
        return res - 1
