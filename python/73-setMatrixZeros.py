class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return 
        def setZero(i, j):
            for x in range(len(matrix)):
                matrix[x][j] = str((matrix[x][j]))
            for y in range(len(matrix[0])):
                matrix[i][y] = str((matrix[i][y]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 0:
                    setZero(i, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if type(matrix[i][j]) == str:
                    matrix[i][j] = 0
                    
