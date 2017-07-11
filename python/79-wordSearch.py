class Solution(object):
    def exist(self, board, word):
        lx = len(board)
        ly = len(board[0])
        def match(x, y, p):
            if p == len(word):
                return True
            elif 0 <= x < lx and 0 <= y < ly:
                if board[x][y] == word[p]:
                    board[x][y] = '$'
                    res = match(x - 1, y, p + 1) or match(x + 1, y, p + 1) or\
                              match(x, y - 1, p + 1) or match(x, y + 1, p + 1)
                    board[x][y] = word[p]
                    return res
            return False
        for i in range(lx):
            for j in range(ly):
                if match(i, j, 0):
                    return True
        return False
