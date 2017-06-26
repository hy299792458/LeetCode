class Solution(object):
    def solve(self, board):
        if board:
            lx = len(board)
            ly = len(board[0])
            zeros = set()
            for i in range(lx):
                if board[i][0] == 'O':
                    zeros.add((i, 0))
                if board[i][ly - 1] == 'O':
                    zeros.add((i, ly - 1))
            for j in range(ly):
                if board[0][j] == 'O':
                    zeros.add((0, j))
                if board[lx - 1][j] == 'O':
                    zeros.add((lx - 1, j))
            listZeros = list(zeros)
            p = 0
            while p < len(zeros):
                x, y = listZeros[p]
                for nx, ny in {(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)}:
                    if 0 <= nx < lx and 0 <= ny < ly:
                        if board[nx][ny] == 'O' and (nx, ny) not in zeros:
                            zeros.add((nx, ny))
                            listZeros.append((nx, ny))
                p += 1
            for i in range(lx):
                for j in range(ly):
                    if board[i][j] == 'O' and (i, j) not in zeros:
                        board[i][j] = 'X'
