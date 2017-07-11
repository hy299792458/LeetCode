class Solution(object):
    def getHint(self, secret, guess):
        A = B = 0
        c1 = {}
        c2 = {}
        for a, b in zip(secret, guess):
            if a == b:
                A += 1
            c1[a] = c1.get(a, 0) + 1
            c2[b] = c2.get(b, 0) + 1
        for k in c1:
            B += min(c1.get(k, 0), c2.get(k, 0))
        return str(A) + 'A' + str(B - A) + 'B'
