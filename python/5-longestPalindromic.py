class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        i = 0.0
        re = ''
        while i < length:
            if i % 1 == 0:
                l = r = int(i)
            else:
                l = int(i)
                r = l + 1
            while l >= 0 and r < length and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(re):
                re = s[l + 1: r]
            i += 0.5
        return re