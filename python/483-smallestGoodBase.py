class Solution(object):
    def smallestGoodBase(self, n):
        n = int(n)
        for k in range(int(math.log(n, 2)), 1, -1):
            q = int(n ** k ** -1)
            if (1 - q ** (k + 1)) / (1 - q) == n:
                return str(q)
        return str(n - 1)
