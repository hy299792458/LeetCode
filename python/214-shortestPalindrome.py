class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return s
        ins = s[::-1]
        for r in range(len(s) + 1):
            if s.startswith(ins[r:]):
                return ins[:r] + s
