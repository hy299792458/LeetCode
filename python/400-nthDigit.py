class Solution(object):
    def findNthDigit(self, n):
        n -= 1
        l = 1
        reduce = 9
        while n >= reduce * l:
            n -= reduce * l
            reduce *= 10
            l += 1
        num = 10 ** (l - 1) + n / l
        return int(str(num)[n % l])
            
