import numpy as np

class Board:
    def __init__(self,row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.board = [[" " for i in range(row_size)] for j in range(col_size)]


    def display_board(self):
        for i in range(self.row_size):
            for j in range(self.col_size):
                print("|" + str(self.board[i][j]), end=" ")
            print("\n--------")
        print()

    def check_win_condition(self, token):
        return False