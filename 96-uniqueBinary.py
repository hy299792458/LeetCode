class Solution(object):
    store = {1:1, 0: 1}
    def numTrees(self, n):
        if n in self.store:
            return self.store[n]
        re = 0
        for i in range(n):
            re += self.numTrees(i) * self.numTrees(n - i - 1)
        self.store[n] = re
        return re
