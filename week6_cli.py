# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from week6_logic import TicTacToeGame
import math


if __name__ == '__main__':


    # Introduction to the game and setting out the rules

    print("\n\n-------------------------------\nWelcome to Tic-Tac-Toe!!\n-------------------------------")

    print("\n\nChoose game type: 1 player or 2 player?")
    game_type = input("\n\nEnter 1 for one player game against bot and 2 for 2 player game: ")
    start_game = TicTacToeGame(game_type)