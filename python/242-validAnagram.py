class Solution(object):
    def isAnagram(self, s, t):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) - 1
        return all(c == 0 for c in count.values())
