from enum import Enum

from models.coordinates import Coordinates


class CellStatus(Enum):
    ALIVE = 1
    DESTROYED = 2


class Position:

    def __init__(self, x, y):
        self.coordinates = Coordinates(x, y)
        self.status = CellStatus.ALIVE


class Ship:

    def __init__(self, origine, direction, cell_num):
        self._positions = []
        self.displayCaracter = str(cell_num)
        self.set_positions(origine, direction, cell_num)

    def set_positions(self, origine, direction, cell_num):

        if direction == 1:
            x_offset = 1
            y_offset = 0
        elif direction == 2:
            x_offset = 0
            y_offset = 1
        elif direction == 3:
            x_offset = -1
            y_offset = 0
        elif direction == 4:
            x_offset = 0
            y_offset = -1

        for item in range(cell_num):
            self._positions.append(Position(origine.x + (x_offset * item), origine.y + (y_offset * item)))

    def has_position(self, x, y):
        for position in self._positions:
            if position.coordinates.x == x and position.coordinates.y == y:
                return True
        return False
