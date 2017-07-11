class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        store = {}
        def match(i, j):
            if (i, j) in store:
                return store[(i, j)]
            if i == len(s1) and j == len(s2):
                res = True
            else:
                c1 = s1[i] if i < len(s1) else None
                c2 = s2[j] if j < len(s2) else None
                res = False
                if c1 == s3[i + j]:
                    res |= match(i + 1, j)
                if c2 == s3[i + j]:
                    res |= match(i, j + 1)
            store[(i, j)] = res
            return res
        return match(0, 0)
