class Solution(object):
    def magicalString(self, n):
        if n == 0:
            return 0
        mag = [1,2,2]
        temp = 1
        res = 1
        p = 2
        for _ in range(n - 2):
            mag += [temp] * mag[p]
            if mag[p] == 1:
                res += 1
            p += 1
            if temp == 1:
                temp = 2
            else:
                temp = 1
        return res
