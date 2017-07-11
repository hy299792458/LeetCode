class Solution(object):
    def findComplement(self, num):
        num = abs(num)
        total = 1
        while total <= num:
            total *= 2
        return total - num - 1
