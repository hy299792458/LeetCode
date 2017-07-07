class Solution(object):
    def superPow(self, a, b):
        res = 1
        mul = a
        for num in b[::-1]:
            res *= mul ** num
            mul = mul ** 10
            mul %= 1337
            res %= 1337
        return res
