# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from week8_final_logic import Game, Human, Bot


if __name__ == '__main__':


    # Introduction to the game and setting out the rules

    print("\n\n-------------------------------\nWelcome to Tic-Tac-Toe!!\n-------------------------------")

    print("\n\nChoose game type: 1 player or 2 player?")
    game_type = input("\n\nEnter 1 for one player game against bot and 2 for 2 player game: ")

    if (int(game_type) ==  1):

        start_game = Game(Human(),Bot())
        start_game.run()

    else:

        start_game = Game(Human(),Human())
        start_game.run()


    # game_board = Board()
    # game_board.set(0,0,1)
    # game_board.get(0,0)
    # game_board.print_board()