class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []
        lx = len(matrix)
        ly = len(matrix[0])
        res = []
        d = -1
        for l in range(lx + ly - 1):
            left = max(0, l - ly + 1)
            right = min(lx, l + 1)
            temp = [matrix[i][l - i] for i in range(left, right)]
            res += temp[::d]
            d *= -1
        return res
