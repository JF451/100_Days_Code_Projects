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
        my_dict = {}

        # now return a draw
        # Horizontal winning condition
        for i in range(len(self.board)):
            count = 0
            for j in range(len(self.board[i])):
                if self.board[i][j] == token:
                    count += 1
            if count == 3:
                return True

        for i in range(len(self.board)):
            count = 0
            for j in range(len(self.board[i])):
                if self.board[j][i] == token:
                    count += 1
            if count == 3:
                return True


        #check diagonals
        if self.board[0][0] == token and self.board[1][1] == token and self.board[2][2]:
            return True
        if self.board[0][2] == token and self.board[1][1] == token and self.board[2][0]:
            return True



        return False