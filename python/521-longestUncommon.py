class Solution(object):
    def findLUSlength(self, a, b):
        return -1 if a == b else max(map(len, [a, b]))
