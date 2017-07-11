class Solution(object):
    def updateBoard(self, board, click):
        lx = len(board)
        ly = len(board[0])
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        seen = set()
        def dfs(pos):
            x, y = pos
            adj = {(x-1, y-1), (x, y-1), (x+1, y-1),
                    (x-1, y), (x+1,y), (x-1, y+1), (x, y+1), (x+1, y+1)}
            count = 0
            for nx, ny in adj:
                if 0 <= nx <lx and 0 <= ny < ly:
                    if board[nx][ny] == 'M':
                        count += 1
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for nx, ny in adj:
                    if (nx, ny) in seen:
                        continue
                    seen.add((nx, ny))
                    if 0 <= nx <lx and 0 <= ny < ly:
                        dfs((nx, ny))
        dfs((x, y))
        return board
