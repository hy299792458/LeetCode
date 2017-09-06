class Solution(object):
    def shoppingOffers(self, price, special, needs):
        self.res = float('inf')
        def dfs(pos, left, cost):
            if pos == len(special):
                for n, p in zip(left, price):
                    cost += n * p
                self.res = min(self.res, cost)
            else:
                can = float('inf')
                for l, o in zip(left, special[pos]):
                    if o == 0:
                        continue
                    can = min(l / o, can)
                for c in range(can + 1):
                    newLeft = [left[i] - c * special[pos][i] for i in range(len(left))]
                    dfs(pos + 1, newLeft, cost + c * special[pos][-1])
        dfs(0, needs, 0)
        return self.res
