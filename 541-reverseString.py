class Solution(object):
    def reverseStr(self, s, k):
        p = 0
        direc = -1
        re = []
        while p < len(s):
            temp = s[p:p+k]
            re.append(temp[::direc])
            p += k
            direc *= -1
        return ''.join(re)
