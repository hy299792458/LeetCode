class Solution(object):
    def toHex(self, num):
        num = num & 0xffffffff
        res = []
        while num:
            temp = num % 16
            if temp > 9:
                res.append(chr(ord('a') + temp - 10))
            else:
                res.append(str(temp))
            num /= 16
        return ''.join(res[::-1]) if res else "0"
