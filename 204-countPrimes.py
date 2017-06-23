class Solution(object):
    def countPrimes(self, n):
        num = [True for _ in range(n + 1)]
        num[: 2] = [False] * 2
        for i in xrange(len(num)):
            if num[i]:
                pos = 2 * i
                while pos < len(num):
                    num[pos] = False
                    pos += i
        return sum(num[:-1])
