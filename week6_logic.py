import random
import math

class TicTacToeGame:

	board = None
	winner = None
	turn = None
	game_type = None
	input_index = None

	def __init__(self, game_type) -> None:

		self.game_type = game_type

		self.board = [
		[None, None, None],
		[None, None, None],
		[None, None, None],
		]

		self.winner = None
		self.turn = 'X'

		print("Rules of the game:")
		print("Player 1 has symbol X")
		print("Player 2 has symbol O (Capital O)")

		# print(game_type)
		# print(type(game_type))

		self.game_type = int(self.game_type)
		# print(type(self.game_type))

		if self.game_type == 1:
			print("\n\n------------------ Playing againt bot! -----------------------")
			self.one_player_game()
		elif self.game_type == 2:
			self.two_player_game()



	def one_player_game(self):
		while self.winner == None:
			# print("\n\n-------------------------------\n")


			# TODO: Show the board to the user.
			print("\nCurrent board:" )
			self.print_board(self.board)
			print("\n----> TODO: take a turn! Player ", self.turn)
			self.print_board_positions(self.board)

			# TODO: Input a move from the player.
			print("\n==> Player ", self.turn)
			

			# TODO: Update who's turn it is.
			if self.turn == 'O':
				print("\n\nBot playing!!")
				self.bot_play(self.turn)
				self.winner = self.get_winner(self.board)


			elif self.turn == 'X':
				self.input_index = input("Choose a position to add your symbol: ")
				if not isinstance(int(self.input_index), int):
					raise TypeError("Please enter an integer")

				# TODO: Update the board.
				self.board = self.update_board(self.board, self.input_index, self.turn)
				self.winner = self.get_winner(self.board)


			self.turn = self.other_player(self.turn)


		if self.winner!= None:
			print("\n---------------------------------------------")
			print("--------- Yayyy, player ", self.other_player(self.turn) , " won! ------------")
			print("---------------------------------------------")





	def bot_play(self, turn):
		board_x = random.randint(0,2)
		board_y = random.randint(0,2)

		if (self.board[board_x][board_y] != None):
			self.bot_play(self.turn)
		else:
			print('----> Bot chose index ', board_x, ', ', board_y)
			self.board[board_x][board_y] = 'O'




	def two_player_game(self):
		while self.winner == None:
			print("\n\n-------------------------------\n")

			# TODO: Show the board to the user.
			print("\nCurrent board:" )
			self.print_board(self.board)
			print("\nTODO: take a turn! Player ", self.turn)
			self.print_board_positions(self.board)

			# TODO: Input a move from the player.
			print("\n==> Player ", self.turn)
			self.input_index = input("Choose a position to add your symbol: ")
			if not isinstance(int(self.input_index), int):
				raise TypeError("Please enter an integer")

			# TODO: Update the board.
			self.board = self.update_board(self.board, self.input_index, self.turn)

			# TODO: Update who's turn it is.
			self.turn = self.other_player(self.turn)



			self.winner = self.get_winner(self.board)

		if self.winner!= None:
			print("\n---------------------------------------------")
			print("--------- Yayyy, player ", self.other_player(self.turn), " won! ------------")
			print("---------------------------------------------")


	def print_board(self, board):
	# Function takes a board as an input and prints it
		for row in self.board:
			print(row)


	def print_board_positions(self, board):

	# Display various positions on the board where values can be entered
		print("\nBoard square positions available to pick (the # ones are taken, you can pick any of the numbers):")

		x = [[1,2,3], [4, 5, 6], [7, 8, 9]]

		for i in range(0,9):
			board_x = int(i / 3)
			board_y = math.ceil(i % 3)
			if board[board_x][board_y] != None:
				x[board_x][board_y] = ("#")

		for row in x:
			print(row)



	def update_board(self, board, index, turn):

		index = int(index)

		assert index > 0 and index < 10

		if (index < 1  or index > 9):
			print("Sorry, enter a number between 1 and 9")


		index = index - 1
		board_x = int(index / 3)
		board_y = math.ceil(index % 3)
		if(self.board[board_x][board_y] == None):
			self.board[board_x][board_y] = self.turn
		else:
			print("Choose an empty location! This slot is taken")
			self.input_index = input("\nChoose a position to add your symbol: ")
			self.update_board(self.board, self.input_index, self.turn)

		return self.board


	def get_winner(self, board):
		"""Determines the winner of the given board.
		Returns 'X', 'O', or None."""

		if(self.board[0][0] == self.board[0][1] == self.board[0][2]):
			self.winner = self.board[0][0]
			# print(winner + (" first row"))

		elif(self.board[1][0] == self.board[1][1] == self.board[1][2]):
			self.winner = self.board[1][0]
		# print(winner + (" middle row"))

		elif(self.board[2][0] == self.board[2][1] == self.board[2][2]):
			self.winner = self.board[2][0]
			# print(winner + (" last row"))

		elif((self.board[0][0] == self.board[1][1] == self.board[2][2])):
			self.winner = self.board[0][0]
			# print(winner + (" left diagonal"))
			
		elif((self.board[2][0] == self.board[1][1] == self.board[0][2])):
			self.winner = self.board[2][0]
			# print(winner + (" right diagonal"))

		elif((self.board[0][0] == self.board[1][0] == self.board[2][0])):
			self.winner = self.board[0][0]
			# print(winner + (" first column"))

		elif((self.board[0][1] == self.board[1][1] == self.board[2][1])):
			self.winner = self.board[0][1]
			# print(winner + (" middle column"))

		elif((self.board[0][2] == self.board[1][2] == self.board[2][2])):
			self.winner = self.board[0][2]
			# print(winner + (" last column"))
		else:
			self.winner = None

		return self.winner


	def other_player(self, player):
		"""Given the character for a player, returns the other player."""
		assert player != None
		if player == 'X':
			return 'O'  # FIXME
		else:
			return 'X'



	def print_board_positions(self, board):

		# Display various positions on the board where values can be entered
		print("\nBoard square positions available to pick (the # ones are taken, you can pick any of the numbers):")

		x = [[1,2,3], [4, 5, 6], [7, 8, 9]]

		for i in range(0,9):
			board_x = int(i / 3)
			board_y = math.ceil(i % 3)
			if self.board[board_x][board_y] != None:
				x[board_x][board_y] = ("#")

		for row in x:
			print(row)

