import termcolor

class Board:
    def __init__(self):
        self.board = [[" " for i in range(8)] for j in range(8)]

        for i in range(8):
            self.board[6][i] = "♟ ︎"
            self.board[1][i] = "♙ "

        self.board[0][0] = "♖ "
        self.board[0][1] = "♘ "
        self.board[0][2] = "♗ "
        self.board[0][3] = "♕ "
        self.board[0][4] = "♔ "
        self.board[0][5] = "♗ "
        self.board[0][6] = "♘ "
        self.board[0][7] = "♖ "
        self.board[7][0] = "♜ "
        self.board[7][1] = "♞ "
        self.board[7][2] = "♝ "
        self.board[7][3] = "♛ "
        self.board[7][4] = "♚ "
        self.board[7][5] = "♝ "
        self.board[7][6] = "♞ "
        self.board[7][7] = "♜ "

    def print_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                
                if self.board[i][j] == 0:
                    termcolor.cprint(self.board[i][j], "grey", "on_white", end="")

                else:
                    termcolor.cprint(self.board[i][j], "grey", "on_grey", end="")

                if j == 7:
                    print("\n", end="")

board = Board()
board.print_board()
