"""Windmill.py
Windmill model classes and helpers

Most important asset in-game
"""

class Windmill(object):
    _kind = ""
    _cost = 0
    _drain_radius = 0
    _height = 0
    _power = 0
    _damage = 0

    def __init__(self, kind="Simple Windmill", cost=10000, drain_radius=10, height=10, power=10, damage=0):
        self._kind = kind
        self._cost = cost
        self._drain_radius = drain_radius
        self._height = height
        self._power = power
        self._damage = damage

    