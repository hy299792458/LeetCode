class Solution(object):
    def getPermutation(self, n, k):
        choice = [str(i + 1) for i in range(n)]
        mod = 1
        for i in xrange(1, n):
            mod *= i
        k -= 1
        res = []
        for i in xrange(n - 1, 0, -1):
            res.append(choice[k / mod])
            k %= mod
            mod /= i
            choice.remove(res[-1])
        res += choice
        return ''.join(res)
