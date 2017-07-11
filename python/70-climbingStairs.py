class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(n - 2):
            a, b = b, a + b
        return b
