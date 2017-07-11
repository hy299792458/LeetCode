class Solution(object):
    def convertToBase7(self, num):
        sig = '-' if num < 0 else ''
        if num == 0:
            return '0'
        num = abs(num)
        re = []
        while num:
            re.append(num % 7)
            num /= 7
        return sig + ''.join(map(str, re[::-1]))
