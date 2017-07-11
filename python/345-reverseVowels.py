class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        l = 0
        r = len(s) - 1
        while True:
            while l < len(s) and s[l] not in "aeiouAEIOU":
                l += 1
            while r >=0 and s[r] not in "aeiouAEIOU":
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                return ''.join(s)
