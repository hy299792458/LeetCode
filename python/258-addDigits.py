class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return num % 9 if num % 9 else 9
