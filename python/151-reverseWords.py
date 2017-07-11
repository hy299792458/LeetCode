class Solution(object):
    def reverseWords(self, s):
        words = []
        temp = []
        for char in s:
            if char == ' ':
                if temp:
                    words.append(''.join(temp))
                temp = []
            else:
                temp.append(char)
        if temp:
            words.append(''.join(temp))
        return ' '.join(words[::-1])
