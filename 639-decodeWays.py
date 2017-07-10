class Solution(object):
    def numDecodings(self, s):
        if not s:
            return 0
        mod = 10 ** 9 + 7
        dp = [1]
        if s[0] == '*':
            dp.append(9)
        elif s[0] != '0':
            dp.append(1)
        else:
            dp.append(0)
        for i in xrange(1, len(s)):
            a, b = dp
            temp = 0
            if s[i -1] == s[i] == '*':
                temp = (temp + a * 15) % mod
            elif s[i - 1] == '*':
                if s[i] < '7':
                    temp = (temp + a * 2) % mod
                else:
                    temp = (temp + a) % mod
            elif s[i] == '*':
                if s[i-1] == '1':
                    temp = (temp + a * 9) % mod
                elif s[i - 1] == '2':
                    temp = (temp + a * 6) % mod
                else:
                    pass
            else:
                if s[i - 1] != '0':
                    if s[i - 1] == '1':
                        temp = (temp + a) % mod
                    elif s[i - 1] == '2' and s[i] < '7':
                        temp = (temp + a) % mod
                    else:
                        pass
                else:
                    pass
            if s[i] != '0':
                if s[i] == '*':
                    temp = (temp + b * 9) % mod
                else:
                    temp = (temp + b) % mod
            dp = [b, temp]
        return dp[1]
