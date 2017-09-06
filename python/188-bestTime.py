class Solution(object):
    def maxProfit(self, k, prices):
        if not prices:
            return 0

        n = len(prices)
        if k >= n // 2:
            return sum(
                x - y
                for x, y in zip(prices[1:], prices[:-1])
                if x > y)

        profits = [0] * n
        for j in range(k):
            # Update new_profits
            max_all = max_prev = max_here = 0
            for i in range(1, n):
                profit = prices[i] - prices[i-1]
                max_here = max(max_here + profit, max_prev + profit, max_prev)
                max_prev = profits[i]
                profits[i] = max_all = max(max_all, max_here)
        return profits[-1]
