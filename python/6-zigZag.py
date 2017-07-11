class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        slot = [[] for _ in range(numRows)]
        i = 0
        mv = 1
        for char in s:
            slot[i].append(char)
            i += mv
            if i == 0:
                mv = 1
            if i == len(slot) - 1:
                mv = -1
        return ''.join(map(lambda x: ''.join(x), slot))
            
