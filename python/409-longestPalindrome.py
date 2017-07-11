class Solution(object):
    def longestPalindrome(self, s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        re = sum(i - i % 2 for i in count.values())
        if re < len(s):
            re += 1
        return re 
