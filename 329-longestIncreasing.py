class Solution(object):
    def longestIncreasingPath(self, matrix):
        re = 0
        if not matrix:
            return re
        lx, ly = len(matrix), len(matrix[0])
        store = {}
        def dfs(i, j):
            if (i,j) in store:
                return store[(i,j)]
            re = 1
            if i > 0 and matrix[i-1][j] < matrix[i][j]:
                re = max(re, dfs(i-1, j) + 1)
            if j > 0 and matrix[i][j-1] < matrix[i][j]:
                re = max(re, dfs(i, j-1) + 1)
            if i < lx - 1 and matrix[i+1][j] < matrix[i][j]:
                re = max(re, dfs(i+1, j) + 1)
            if j < ly - 1 and matrix[i][j+1] < matrix[i][j]:
                re = max(re, dfs(i, j+1) + 1)
            store[(i,j)] = re
            return re
        for i in range(lx):
            for j in range(ly):
                re = max(re, dfs(i, j))
        return re 
