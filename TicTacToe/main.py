from Board import Board
from HumanPlayer import HumanPlayer

#Create Board
board = Board(3,3)
#Create two human players
player1 = HumanPlayer("X")
player2 = HumanPlayer("O")
#Ask users to enter coordinates to place object
game_over = False
while not game_over:
    game_counter = 0

    a = tuple(int(x) for x in input("Enter move for player 1:\n " ).split(","))
    #Check for win condition
    player1.set_piece(board, a[0], a[1])
    game_counter += 1
    game_over = board.check_win_condition(player1.side)
    board.display_board()

    if game_over == True:
        print(f"Player1 {player1.side} wins")
        break

    if game_counter == 9 and game_over == False:
        print("DRAW")
        break


    b = tuple(int(x) for x in input("Enter move for player 2:\n ").split(","))
    player2.set_piece(board, b[0], b[1])
    game_counter += 1

    game_over = board.check_win_condition(player2.side)
    #Disaply board beteeen moves
    board.display_board()

    if game_over == True:
        print(f"Player2 {player1.side} wins")
        break

    if game_counter == 9 and game_over == False:
        print("DRAW")
        break

