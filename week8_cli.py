# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from week8_final_logic import Game, Human, Bot
import numpy as np
import pandas as pd

if __name__ == '__main__':


    # Introduction to the game and setting out the rules

    print("\n\n-------------------------------\nWelcome to Tic-Tac-Toe!!\n-------------------------------")

    print("\n\nChoose game type: 1 player or 2 player?")

    game_type = input("\n\nEnter 1 for one player game against bot and 2 for 2 player game, and 3 for Bot vs Bot game ")

    if (int(game_type) ==  1):

        start_game = Game(Human(),Bot())
        start_game.run()

    elif(int(game_type) ==  2):

        start_game = Game(Human(),Human())
        start_game.run()

    elif(int(game_type) ==  3):

        start_game = Game(Bot(),Bot())
        start_game.run()




## Ran the script with start_game = Game(Bot(),Bot()) 50 times using the command given below to collect stats
# for x in {1..50}; do (python week8_cli.py) & done 
