class Solution(object):
    def reverseWords(self, s):
        words = s.split(' ')
        reWords = map(lambda x: x[::-1], words)
        return ' '.join(reWords)
