class Solution(object):
    def maxProduct(self, words):
        def mask(word):
            re = 0
            for char in word:
                re |= 2 ** (ord(char) - ord('a'))
            return re
        masks = map(mask, words)
        re = 0
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                if masks[i] & masks[j] == 0:
                    re = max(re, len(words[i]) * len(words[j]))
        return re
