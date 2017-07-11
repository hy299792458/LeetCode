class Solution(object):
    def numberOfArithmeticSlices(self, A):
        res = 0
        i = 0
        while i < len(A) - 1:
            diff = A[i + 1] - A[i]
            count = 1
            j = i + 2
            while j < len(A) and A[j] - A[i + 1] == count * diff:
                res += count
                count += 1
                j += 1
            i = j - 1
        return res
