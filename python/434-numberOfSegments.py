class Solution(object):
    def countSegments(self, s):
        re = filter(lambda x: x != '', s.split(' '))
        return len(re)
