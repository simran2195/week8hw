import sys
import random
import math

class Board:

	# board = None
	winner = None
	
	def __init__(self):
		self.board = [
		[None, None, None],
		[None, None, None],
		[None, None, None],
		]

	def print_board(self):
		for row in self.board:
			print(row)


	def get(self, x, y):
		return self.board[x][y] 

	def set(self, x, y, value):
		self.board[x][y] = value


	def print_board_positions(self):
	# Display various positions on the board where values can be entered
		print("\nBoard square positions available to pick (the # ones are taken, you can pick any of the numbers):")

		x = [[1,2,3], [4, 5, 6], [7, 8, 9]]

		for i in range(0,9):
			board_x = int(i / 3)
			board_y = math.ceil(i % 3)
			if self.board[board_x][board_y] != None:
				x[board_x][board_y] = '#'
		

		for row in x:
			print(row)

	def get_winner(self):
		"""Determines the winner of the given board.
		Returns 'X', 'O', or None."""

		if(self.get(0,0) == self.get(0,1) == self.get(0,2)):
			self.winner = self.get(0,0)
			# print(winner + (" first row"))

		elif(self.get(1,0) == self.get(1,1) == self.get(1,2)):
			self.winner = self.get(1,0)
		# print(winner + (" middle row"))

		elif(self.get(2,0) == self.get(2,1) == self.get(2,2)):
			self.winner = self.get(2,0)
			# print(winner + (" last row"))

		elif((self.get(0,0) == self.get(1,1) == self.get(2,2))):
			self.winner = self.get(0,0)
			# print(winner + (" left diagonal"))
			
		elif((self.get(2,0) == self.get(1,1) == self.get(0,2))):
			self.winner = self.get(2,0)
			# print(winner + (" right diagonal"))

		elif((self.get(0,0) == self.get(1,0) == self.get(2,0))):
			self.winner = self.get(0,0)
			# print(winner + (" first column"))

		elif((self.get(0,1) == self.get(1,1) == self.get(2,1))):
			self.winner = self.get(0,1)
			# print(winner + (" middle column"))

		elif((self.get(0,2) == self.get(1,2) == self.get(2,2))):
			self.winner = self.get(0,2)
			# print(winner + (" last column"))
		else:
			self.winner = None

		return self.winner

class Game:
	def __init__(self, playerX, playerO):
		self._board = Board()
		self._playerX = playerX
		self._playerO = playerO
		self.current = self._playerX
		self.turn = 'X' # X plays first by default

	def other_player(self, player):
		"""Given the character for a player, returns the other player."""
		assert player != None
		if player == 'X':
			self.current = self._playerO
			return 'O'  # FIXME
		else:
			self.current = self._playerX
			return 'X'

	def run(self):
		move = 0
		while move<9:
			print("\n---------------------------------------------")

			print("Play your turn")
			print("\nCurrent board:" )
			self._board.print_board()
			print("\n----> TODO: take a turn! Player ", self.turn)
			self._board.print_board_positions()
			self.current.play(self.turn, self._board)
			if self._board.get_winner():

				print("\n---------------------------------------------")
				print("--------- Yayyy, player ", self.turn , " won! Congratulations ------------")
				print("---------------------------------------------")

				sys.exit("Thank you for playing!!")
			move += 1
			self.turn = self.other_player(self.turn)
		print('Draw')



class Bot:
	def play(self, turn, board):
		board_x = random.randint(0,2)
		board_y = random.randint(0,2)

		if (board.get(board_x,board_y)!= None):
			self.play(turn, board)
		else:
			print('----> Bot chose index ', board_x, ', ', board_y)
			board.set(board_x,board_y,'O')
			# bot has O by default
			return board

class Human:
	def play(self, turn, board ):
		input_index = int(input("\nChoose a position to add your symbol: "))
		if not isinstance(int(input_index), int):
			raise TypeError("Please enter an integer")

		if (input_index < 1  or input_index > 9):
			print("Sorry, enter a number between 1 and 9")


		index = input_index - 1
		board_x = int(index / 3)
		board_y = math.ceil(index % 3)

		if(board.get(board_x,board_y) == None):
			board.set(board_x, board_y, turn)
		else:
			print("Choose an empty location! This slot is taken")
			# self.input_index = input("\nChoose a position to add your symbol: ")
			self.play(turn, board)

		return board
