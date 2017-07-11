class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        def Comb(n):
            re = 1
            for i in range(n):
                if i == 0:
                    re *= 9
                else:
                    re *= (10-i)
            return re
        return sum(map(Comb, [i for i in range(n+1)]))
