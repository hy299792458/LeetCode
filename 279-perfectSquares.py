class Solution(object):
    store = {0: 0}
    def numSquares(self, n):
        if n in self.store:
            return self.store[n]
        else:
            res = 4
            for i in range(1, int(math.sqrt(n)) + 1):
                res = min(res, self.numSquares(n - i * i) + 1)
            self.store[n] = res
            return res
