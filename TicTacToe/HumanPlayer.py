from Board import Board


class HumanPlayer:
    def __init__(self, side):
        self.side = side

    def set_piece(self, board, x, y):
        board.board[x][y] = self.side

