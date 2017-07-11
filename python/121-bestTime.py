class Solution(object):
    def maxProfit(self, prices):
        re = 0
        low = float('inf')
        for p in prices:
            re = max(re, p - low)
            low = min(low, p)
        return re
