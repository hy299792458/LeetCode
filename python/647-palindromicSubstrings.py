class Solution(object):
    def countSubstrings(self, s):
        cnt = len(s)
        def match(s):
            return s == s[::-1]
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1):
                if match(s[i : j]):
                    cnt += 1
        return cnt
