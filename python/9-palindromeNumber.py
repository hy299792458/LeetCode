class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        l = 0
        while x / 10 ** l:
            l += 1
        r = 0
        l -= 1
        while r < l:
            if x / 10 ** l % 10 == x / 10 ** r % 10:
                l -= 1
                r += 1
            else:
                return False
        return True
