class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        store = obstacleGrid[:][:]
        lx, ly = len(store), len(store[-1])
        for i in range(lx):
            for j in range(ly):
                if obstacleGrid[i][j] == 1:
                    store[i][j] = 0
                else:
                    store[i][j] = int(i == 0 and j == 0)
                    store[i][j] += store[i-1][j] * (i > 0) + store[i][j-1] * (j > 0)
        return store[-1][-1]
