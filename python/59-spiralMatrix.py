class Solution(object):
    def generateMatrix(self, n):
        re = [[None for _ in range(n)] for _ in range(n)]
        add = [0, 1]
        num = 1
        x, y = 0, 0
        for num in range(1, n * n + 1):
            re[x][y] = num
            if x + add[0] < 0 or x + add[0] >= n \
            or y + add[1] < 0 or y + add[1] >= n \
            or re[x+add[0]][y+add[1]] != None:
                add = add[1], -add[0]
            x += add[0]
            y += add[1]
        return re
