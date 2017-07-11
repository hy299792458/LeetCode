class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == ')' and dp[i - 1]:
                    last = i - dp[i - 1] - 1
                    if last >= 0 and s[last] == '(':
                        dp[i] = dp[i - 1] + 2
                        if last - 1 >= 0 and s[last -1] == ')':
                            dp[i] += dp[last - 1]
                elif s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i > 1 else 2
        #print dp
        return max(dp)
