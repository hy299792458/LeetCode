class Solution(object):
    def solveNQueens(self, n):
        self.res = []
        def fill(p, temp, cols, lslot, rslot):
            if p == n:
                self.res.append(temp)
            for i in range(n):
                if i not in cols and i + p not in rslot and i - p not in lslot:
                    line = ['.'] * n
                    line[i] = 'Q'
                    fill(p + 1, temp + [''.join(line)], cols | {i}, lslot|{i - p}, rslot|{i + p})
        fill(0, [], set(), set(), set())
        return self.res
