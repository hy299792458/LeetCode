class Solution(object):
    def findPaths(self, m, n, N, rei, rej):
        mod = 10 ** 9 + 7
        store = [[[0, 0] for _ in range(n)] for _ in range(m)]
        for t in range(N):
            for i in range(m):
                for j in range(n):
                    val = 0
                    for adi, adj in [(i - 1, j),(i + 1, j),(i, j - 1),(i, j + 1)]:
                        if m > adi >= 0 and n > adj >= 0: 
                            val += store[adi][adj][t % 2]
                        else:
                            val += 1
                    store[i][j][(t + 1) % 2] = val % mod
        #print store
        return store[rei][rej][N % 2] % mod
