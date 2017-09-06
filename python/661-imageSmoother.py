class Solution(object):
    def imageSmoother(self, M):
        if not M:
            return []
        x = len(M)
        y = len(M[0])
        res = [[0 for _ in range(y)] for _ in range(x)]
        adj = [(-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 0), (1, 1), (0, 1), (-1, 1)]
        for i in range(x):
            for j in range(y):
                total = 0
                cnt = 0        
                for dx, dy in adj:
                    if 0 <= i + dx < x and 0 <= j + dy < y:
                        cnt += 1
                        total += M[i + dx][j + dy]
                res[i][j] = total / cnt
        return res
