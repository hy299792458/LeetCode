class Solution(object):
    def isSubsequence(self, s, t):
        match = iter(t)
        for char in s:
            if char not in match:
                return False
        return True
