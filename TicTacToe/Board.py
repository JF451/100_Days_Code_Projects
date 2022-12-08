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
        #Check vertical
        vertical_count = 0
        for i in range((self.row_size)):
            for j in range((self.col_size)):
                if self.board[i][j] == token:
                    vertical_count += 1
        print(vertical_count)
        if vertical_count == 3:
            return True

        #Check horizontal
        horizontal_count = 0
        for i in range((self.row_size)):
            for j in range((self.col_size)):
                if self.board[j][i] == token:
                    horizontal_count += 1
        if horizontal_count == 3:
            return True

        #Check diagonals
        diagonal_count1 = 0
        diagonal_count2 = 0
        if self.board[0][0] == token and self.board[1][1] == token and self.board[2][2] == token:
            diagonal_count1 += 1
        if self.board[0][2] == token and self.board[1][1] == token and self.board[2][0] == token:
            diagonal_count2 += 1

        if diagonal_count1 == 3 or diagonal_count2 == 3:
            return True

        return False