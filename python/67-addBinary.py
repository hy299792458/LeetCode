class Solution(object):
    def addBinary(self, a, b):
        A = [int(num) for num in a[::-1]]
        B = [int(num) for num in b[::-1]]
        res = []
        p1 = p2 = 0
        c = 0
        while p1 < len(A) or p2 < len(B) or c:
            temp = c
            if p1 < len(A):
                temp += A[p1]
            if p2 < len(B):
                temp += B[p2]
            res.append(temp % 2)
            c = temp / 2
            p1 += 1
            p2 += 1
        return ''.join(map(str, res[::-1]))
