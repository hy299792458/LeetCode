class Solution(object):
    def minSteps(self, n):
        facs = dict()
        i = 2
        while i <= n:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n /= i
            facs[i] = cnt
            i += 1
        res = 0
        for k in facs:
            res += facs[k] * k
        return res
