class Solution(object):
    def isValidSudoku(self, board):
        blocks = [[set() for _ in range(3)] for _ in range(3)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in blocks[i / 3][j / 3] or num in rows[i] or num in cols[j]:
                    return False
                blocks[i / 3][j / 3].add(num)
                rows[i].add(num)
                cols[j].add(num)
        return True
