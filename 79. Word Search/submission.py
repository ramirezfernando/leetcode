class Solution:
    def exist(self, board, word):

        ROWS = len(board)
        COLS = len(board[0])

        def wordFound(row, col, i):
            if (row >= ROWS or row < 0 or col >= COLS or col < 0):
                return False
            if board[row][col] != word[i] or board[row][col] == '#':
                return False
            elif i == len(word) - 1:
                return True
            
            tmp = board[row][col]
            board[row][col] = '#'
            up = wordFound(row, col + 1, i + 1)
            down = wordFound(row, col - 1, i + 1)
            left = wordFound(row - 1, col, i + 1)
            right = wordFound(row + 1, col, i + 1)
            board[row][col] = tmp
            return up or down or left or right

        for r in range(ROWS):
            for c in range(COLS):
                if wordFound(r, c, 0):
                    return True
        return False