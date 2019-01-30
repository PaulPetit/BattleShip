from models import utils
from models.grid import Grid
from models.coordinates import Coordinates
from enum import Enum


class Status(Enum):
    HIT = 1
    MISS = 2


class Shot:

    def __init__(self, x, y, status):
        self.coordinates = Coordinates(x, y)
        self.status = status


class Player:

    def __init__(self, name):
        self.name = name
        self._grid = Grid()
        self._shot_list = []

    def show_grid(self, position):
        if position == "right":
            utils.setCursorPos(30, 0)
        print(self.name)
        self._grid.print(position)

    def validate_target(self, x, y):
        """
        Retourne True si le tir n'a pas déjà été effectué
        :param x:
        :param y:
        :return:
        """
        for shot in self._shot_list:
            if shot.coordinates.y == y and shot.coordinates.x == x:
                return False
        return True

    def get_shot(self, x, y):
        for ship in self._grid.shipList:
            pass
            # TODO
