"""Gameboard.py
Game board module for game
"""

from .land import LandTile
from random import randint

class GameBoard(object):
    _board = []

    def __init__(self, x=1000, y=1000):
        self._board = [[LandTile(height=randint(-100, 100)) for j in range(x)] for i in range(y)]
    
    def get_board(self):
        return self._board

    def set_board(self, x, y, item):
        try:
            self._board[x][y].set_asset(item)
        except IndexError:
            print("Selection out of Bounds")
        except Exception:
            print("there's already an asset there")