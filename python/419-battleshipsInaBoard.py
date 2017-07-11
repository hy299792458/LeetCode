class Solution(object):
    def countBattleships(self, board):
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (i - 1 < 0 or board[i - 1][j] == '.') and \
                    (j-1 < 0 or board[i][j - 1] == '.'):
                        count += 1
        return count
        
