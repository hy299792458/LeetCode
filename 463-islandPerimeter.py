class Solution(object):
    def islandPerimeter(self, grid):
        lx = len(grid)
        ly = len(grid[0])
        re = 0
        for i in range(lx):
            for j in range(ly):
                if grid[i][j] == 1:
                    re += 4
                    if i + 1 < lx and grid[i + 1][j] == 1:
                        re -= 2
                    if j + 1 < ly and grid[i][j + 1] == 1:
                        re -= 2
        return re 
