class Solution(object):
    def combine(self, n, k):
        if k == 0:
            return [[]]
        res = []
        for i in range(k,n+1):
            tmp = self.combine(i-1, k-1)
            for x in tmp:
                res.append(x+[i])
        return res
        
