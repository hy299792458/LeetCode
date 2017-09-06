class Solution(object):
    def getRow(self, rowIndex):
        re = [1]
        for _ in range(rowIndex):
            re = [1] + [a + b for a, b in zip(re, re[1:])] + [1]
        return re