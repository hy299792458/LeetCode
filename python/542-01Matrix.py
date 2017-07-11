class Solution(object):
    def updateMatrix(self, matrix):
        if not matrix:
            return []
        lx = len(matrix)
        ly = len(matrix[0])
        zeros = []
        res = [[0 for _ in range(ly)] for _ in range(lx)]
        for i in range(lx):
            for j in range(ly):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        seen = set(zeros)
        count = 1
        while zeros:
            newZeros = []
            for node in zeros:
                x, y = node
                for nx, ny in {(x, y + 1), (x, y -1), (x- 1, y), (x + 1, y)}:
                    if 0 <= nx < lx and 0 <= ny < ly and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        newZeros.append((nx, ny))
                        res[nx][ny] = count
            count += 1
            zeros = newZeros
        return res
