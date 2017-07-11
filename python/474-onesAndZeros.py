class Solution(object):
    def findMaxForm(self, strs, m, n):
        pick = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for num in strs:
            count = [0, 0]
            for char in num:
                count[int(char)] += 1
            for x in xrange(m, -1, -1):
                for y in xrange(n, -1, -1):
                    if x >= count[0] and y >= count[1]:
                        pick[x][y] = max(pick[x][y], pick[x - count[0]][y - count[1]] + 1)
        return pick[-1][-1]
