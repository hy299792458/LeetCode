class Solution(object):
    def minDistance(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(l1):
            dp[i + 1][0] = i + 1
        for j in range(l2):
            dp[0][j + 1] = j + 1
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = min(dp[i][j + 1] + 1, dp[i + 1][j] + 1, dp[i][j])
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        #for l in dp:
        #    print l
        return dp[-1][-1]
