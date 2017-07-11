class Solution(object):
    def isPalindrome(self, s):
        s = s.lower().strip()
        s = filter(lambda x: x.isalpha() or x.isdigit(), [char for char in s])
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
