class Solution(object):
    def maxRotateFunction(self, A):
        s, l = sum(A), len(A)
        temp = re = sum(A[i] * i for i in range(l))
        for i in range(1, l):
            temp += (s - l * A[-i])
            re = max(re, temp)
        return re
