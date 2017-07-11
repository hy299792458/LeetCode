class Solution(object):
    def arrangeCoins(self, n):
        total = 0
        i = 0
        while total <= n:
            i += 1
            total += i
        return i - 1
