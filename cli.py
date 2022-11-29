# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import print_board
from logic import get_winner
from logic import print_board_positions
from logic import update_board
from logic import other_player
import math

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    turn = 'X'

    # Introduction to the game and setting out the rules

    print("\n\n-------------------------------\nWelcome to Tic-Tac-Toe!!\n-------------------------------")
    print("Rules of the game:")
    print("Player 1 has symbol X")
    print("Player 2 has symbol O (Capital O)")



    # functions to implement the functioning of the code

    while winner == None:
        print("\n\n-------------------------------\n")

        # TODO: Show the board to the user.
        print("\nCurrent board:" )
        print_board(board)
        print("\nTODO: take a turn! Player ", turn)
        print_board_positions(board)




        # TODO: Input a move from the player.
        print("\n==> Player ", turn)
        input_index = input("Choose a position to add your symbol: ")
        if not isinstance(int(input_index), int):
            raise TypeError("Please enter an integer")

        # TODO: Update the board.
        board = update_board(board, input_index, turn)

        # TODO: Update who's turn it is.
        turn = other_player(turn)



        winner = get_winner(board)  # FIXME

    if winner!= None:
        print("\n---------------------------------------------")
        print("--------- Yayyy, player ", other_player(turn), " won! ------------")
        print("---------------------------------------------")




