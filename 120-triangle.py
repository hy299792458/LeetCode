class Solution(object):
    def minimumTotal(self, triangle):
        store = {}
        def dfs(i, j):
            if (i, j) in store:
                return store[(i, j)]
            res = triangle[i][j]
            if i < len(triangle) - 1:
                res += min(dfs(i + 1, j), dfs(i + 1, j + 1))
            store[(i, j)] = res
            return res 
        return dfs(0, 0)

#O(n) extra space solution:
class Solution(object):
    def minimumTotal(self, triangle):
        temp = triangle[0]
        for l in triangle[1:]:
            l1 = [a + b for a, b in zip(temp + [float('inf')], l)]
            l2 = [a + b for a, b in zip([float('inf')] + temp, l)]
            temp = [min(a, b) for a, b in zip(l1, l2)]
        return min(temp)
