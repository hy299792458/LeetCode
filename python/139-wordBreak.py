class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            if any(dp[j] and s[j:i] in wordDict for j in range(i)):
                dp[i] = True
        return dp[-1]
