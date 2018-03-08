class Solution:
    def validTicTacToe(self, board):
        board = [[row[0], row[1], row[2]] for row in board]
        numX = numO = 0
        for r in range(3):
            for c in range(3):
                if board[r][c] == 'X':
                    numX += 1
                elif board[r][c] == 'O':
                    numO += 1
        if numX != numO and numX != numO+1:
            return False

        X3, O3 = ['X']*3, ['O']*3
        winX = winO = 0
        for i in range(3):
            row = [board[i][0], board[i][1], board[i][2]]
            if row == X3:
                winX += 1
            elif row == O3:
                winO += 1

            col = [board[0][i], board[1][i], board[2][i]]
            if col == X3:
                winX += 1
            elif col == O3:
                winO += 1

        for dia in ([board[0][0], board[1][1], board[2][2]],
                    [board[2][0], board[1][1], board[0][2]]):
            if dia == X3:
                winX += 1
            elif dia == O3:
                winO += 1

        if winX != 0 and numX != numO+1:
            return False
        if winO != 0 and numX != numO:
            return False
        return True


def test(board, e):
    a = Solution().validTicTacToe(board)
    print(e == a, board, e, a)


board = ["O  ", "   ", "   "]
test(board, False)
board = ["XOX", " X ", "   "]
test(board, False)
board = ["XXX", "   ", "OOO"]
test(board, False)
board = ["XOX", "O O", "XOX"]
test(board, True)
board = ["XXX", "XOO", "XOO"]
test(board, True)
board = ["XXX","XOO","OO "]
test(board, False)
