"""Gameboard.py
Game board module for game
"""

class GameBoard(object):
    _board = []

    def __init__(self, x=1000, y=1000):
        self._board = [[None for j in range(x)] for i in range(y)]
    
    def get_board(self):
        return self._board