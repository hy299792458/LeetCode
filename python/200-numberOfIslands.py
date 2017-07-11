class Solution(object):
    def numIslands(self, grid):
        seen = set()
        if not grid:
            return 0
        lx = len(grid)
        ly = len(grid[0])
        def visit(x, y):
            for nx, ny in [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]:
                if 0 <= nx < lx and 0 <=ny < ly:
                    if (nx, ny) not in seen:
                        seen.add((nx, ny))
                        if grid[nx][ny] == '1':
                            visit(nx, ny)
        res = 0
        for i in range(lx):
            for j in range(ly):
                if (i, j) not in seen and grid[i][j] == '1':
                    seen.add((i, j))
                    res += 1
                    visit(i, j)
        return res
