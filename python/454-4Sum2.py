class Solution(object):
    def fourSumCount(self, A, B, C, D):
        count1 = dict()
        res = 0
        for num1 in A:
            for num2 in B:
                count1[num1 + num2] = count1.get(num1 + num2, 0) + 1
        for num3 in C:
            for num4 in D:
                res += count1.get(-num3 - num4, 0)
        return res
