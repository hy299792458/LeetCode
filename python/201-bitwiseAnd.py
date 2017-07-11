class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        count = 0
        while m != n:
            m /= 2
            n /= 2
            count += 1
        return m << count
