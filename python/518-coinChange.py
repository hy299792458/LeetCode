class Solution(object):
    def change(self, amount, coins):
        store = [0 for _ in range(amount + 1)]
        store[0] = 1
        for c in coins:
            for i in range(amount + 1):
                if i + c <= amount:
                    store[i + c] += store[i]
        return store[-1]
