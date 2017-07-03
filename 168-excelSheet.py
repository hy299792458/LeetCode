class Solution(object):
    def convertToTitle(self, n):
        res = []
        while n:
            n -= 1
            res.append(chr(ord('A') + n % 26))
            n /= 26
        return ''.join(res[::-1])
