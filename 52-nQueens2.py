class Solution(object):
    def totalNQueens(self, n):
        self.res = 0
        def fill(p, temp, cols, lslot, rslot):
            if p == n:
                self.res += 1
            for i in range(n):
                if i not in cols and i + p not in rslot and i - p not in lslot:
                    line = ['.'] * n
                    line[i] = 'Q'
                    fill(p + 1, temp + [''.join(line)], cols | {i}, lslot|{i - p}, rslot|{i + p})
        fill(0, [], set(), set(), set())
        return self.res
