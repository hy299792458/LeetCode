# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l = 0
        r = n + 1
        while True:
            mid = (l + r) / 2
            res = guess(mid)
            if res == -1:
                r = mid
            elif res == 1:
                l = mid + 1
            else:
                return mid
