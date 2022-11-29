import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all functions from logic.py!

    def test_get_winner_X(self):
        board = [
            ['0', None, 'O'],
            ['X', 'X', 'X'],
            ['0', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_get_winner_O(self):
        board = [
            ['0', None, 'O'],
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

    def test_other_player_X(self):
        player = 'X'
        self.assertEqual(logic.other_player(player), 'O')

    def test_other_player_O(self):
        player = 'O'
        self.assertEqual(logic.other_player(player), 'X')


if __name__ == '__main__':
    unittest.main()