class Solution(object):
    def findClosestElements(self, arr, k, x):
        res = []
        for num in arr:
            if len(res) < k:
                res.append(num)
            else:
                if abs(num - x) < abs(res[0] - x):
                    res = res[1: ] + [num]
        return res
