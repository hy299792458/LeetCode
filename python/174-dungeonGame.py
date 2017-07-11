class Solution(object):
    def calculateMinimumHP(self, dungeon):
        lx = len(dungeon)
        ly = len(dungeon[0])
        dp = [[0 for _ in range(ly)] for _ in range(lx)]
        for i in range(lx - 1, -1, -1):
            for j in range(ly - 1, -1, -1):
                temp = -float('inf')
                if i + 1 < lx:
                    temp = max(temp, dp[i + 1][j])
                if j + 1 < ly:
                    temp = max(temp, dp[i][j + 1])
                dp[i][j] = dungeon[i][j] + temp if temp > -float('inf') else dungeon[i][j]
                if dp[i][j] > 0:
                    dp[i][j] = 0
        return -dp[0][0] + 1
