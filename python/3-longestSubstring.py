class Solution(object):
    def lengthOfLongestSubstring(self, s):
        cache = {}
        start = length = 0
        for i in range(len(s)):
            char = s[i]
            if char in cache:
                start = max(start, cache[char] + 1)
            length = max(length, i - start + 1)
            cache[char] = i
        return length
