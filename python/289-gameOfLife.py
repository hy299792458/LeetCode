class Solution(object):
    def gameOfLife(self, board):
        if not board:
            return
        for x in range(len(board)):
            for y in range(len(board[0])):
                adj = {(x, y - 1), (x, y + 1), (x - 1, y - 1),\
                (x - 1, y), (x - 1, y + 1), (x + 1, y),\
                (x + 1, y - 1), (x + 1, y + 1)}
                count = 0
                for nx, ny in adj:
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]): 
                        if board[nx][ny] % 10:
                            count += 1
                if board[x][y] % 10:
                    if count in (2, 3):
                        board[x][y] += 10
                else:
                    if count == 3:
                        board[x][y] += 10
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] /= 10
