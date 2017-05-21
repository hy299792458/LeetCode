class Solution(object):
    def reverse(self, x):
        if x > 2 ** 31 -1 or x < - 2 ** 31:
            return 0
        else:
            sig = -1 if x < 0 else 1
            re = int(str(abs(x))[::-1]) * sig
            return 0 if re > 2 ** 31 - 1 or re < -2**31 else re
