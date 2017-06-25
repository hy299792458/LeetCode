class Solution(object):
    def titleToNumber(self, s):
        re = 0
        for char in s:
            re *= 26
            re += ord(char) - ord('A') + 1
        return re
