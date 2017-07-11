class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        res = [0 for _ in s]
        res[0] = 1
        for i in range(1, len(s)):
            temp = 0
            if int(s[i]) > 0:
                temp += res[i - 1]
            if 9 < int(s[i - 1] + s[i]) < 27:
                if i > 1:
                    temp += res[i - 2]
                else:
                    temp += 1
            res[i] = temp
        #print res
        return res[-1]
