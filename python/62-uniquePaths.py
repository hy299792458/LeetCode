class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        store = {(m-1,n-1):1}
        def DP(i, j):
            if (i, j) in store: 
                return store[(i, j)]
            counts = 0
            if i < m:
                counts += DP(i + 1,j)
            if j < n:
                counts += DP(i, j + 1)
            store[(i, j)] = counts
            return counts
        return DP(0, 0)
