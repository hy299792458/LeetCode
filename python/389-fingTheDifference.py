class Solution(object):
    def findTheDifference(self, s, t):
        re = 0
        for char in s + t:
            re ^= ord(char)
        return chr(re)
