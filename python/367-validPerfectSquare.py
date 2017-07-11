class Solution(object):
    def isPerfectSquare(self, num):
        i = 1
        while num / i > i:
            i += 1
        return i * i == num
