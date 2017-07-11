class Solution(object):
    def rotate(self, matrix):
        l = len(matrix)
        for i in range(l / 2):
            for j in range((l + 1) / 2):
                matrix[i][j], matrix[j][-i - 1],\
                matrix[-i - 1][-j - 1], matrix[-j - 1][i]\
                = matrix[-j - 1][i], matrix[i][j],\
                matrix[j][-i - 1], matrix[-i - 1][-j - 1]
