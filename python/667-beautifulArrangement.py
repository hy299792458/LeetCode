class Solution(object):
    def constructArray(self, n, k):
        res = [1]
        sig = 1
        while(k > 0):
            res.append(res[-1] + sig * k)
            k -= 1
            sig *= -1
        used = set(res)
        for i in range(1, n + 1):
            if i not in used:
                res.append(i)
        return res
