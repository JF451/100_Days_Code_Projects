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
    a = tuple(int(x) for x in input("Enter move for player 1").split(","))
    #Check for win condition
    player1.set_piece(board, a[0], a[1])
    game_over = board.check_win_condition(player1.side)
    board.display_board()

    if game_over == True:
        print(f"PLayer {player1.side} wins")
        break
    b = tuple(int(x) for x in input("Enter move for player 2").split(","))
    player2.set_piece(board, b[0], b[1])

    game_over = board.check_win_condition(player2.side)
    #Disaply board beteeen moves
    board.display_board()

    if game_over == True:
        print(f"PLayer {player2.side} wins")
        break