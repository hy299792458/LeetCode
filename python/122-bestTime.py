class Solution(object):
    def maxProfit(self, prices):
        pro = [a - b for a, b in zip(prices[1:], prices)]
        return sum(p for p in pro if p > 0)
