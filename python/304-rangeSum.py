class NumMatrix(object):

    def __init__(self, matrix):
        res = matrix[:][:]
        for i in range(len(res)):
            for j in range(len(res[0])):
                if i > 0:
                    res[i][j] += res[i - 1][j]
                if j > 0:
                    res[i][j] += res[i][j - 1]
                if i * j > 0:
                    res[i][j] -= res[i - 1][j - 1]
        self.res = res
        

    def sumRegion(self, row1, col1, row2, col2):
        res = self.res[row2][col2]
        if row1:
            res -= self.res[row1 - 1][col2]
        if col1:
            res -= self.res[row2][col1 - 1]
        if row1 * col1:
            res += self.res[row1 - 1][col1 - 1]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
