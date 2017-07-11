class Solution(object):
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        mod = 10 ** int(math.log(n, 10) + 1)
        res = 0
        left, mid, right = 0, 0, n
        while mod:
            left, mid, right = left * 10 + mid, right / mod, right % mod
            #print left, mid, right
            res += left * mod
            if mid > 1:
                res += mod
            elif mid == 1:
                res += right + 1
            mod /= 10
        return res
