import unittest
from models.gameboard import GameBoard

class TestGameBoard(unittest.TestCase):

    def test_gameboard_is_correct_size(self):
        x = Gameboard(10, 10)
        self.assertEqual(10, len(x.get_board()))
        self.assertEqual(10, len(x.get_board()[0]))