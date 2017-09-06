class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        sell = 0
        buy = -prices[0]
        psell = 0
        pbuy = 0
        for p in prices:
            pbuy = buy
            buy = max(psell - p, pbuy)
            psell = sell
            sell = max(pbuy + p, psell)
        return sell
