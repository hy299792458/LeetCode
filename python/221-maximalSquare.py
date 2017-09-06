class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        dp = [[int(n) for n in l] for l in matrix]
        res = max([dp[0][i] for i in range(len(dp[0]))] + [dp[i][0] for i in range(len(dp))])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]!='0':
                    dp[i][j] = (min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])) + 1
                    res = max(res, dp[i][j])
        #print dp
        return res ** 2 
